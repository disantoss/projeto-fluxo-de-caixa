import pandas as pd
import os

# Caminho da sua pasta
caminho = r'C:\Pc Diego\cursos\Projetos Pessoais\Fluxo de Caixa\bases'

# 1. Carregar os arquivos
main = pd.read_csv(os.path.join(caminho, 'checking_account_main.csv'))
secondary = pd.read_csv(os.path.join(caminho, 'checking_account_secondary.csv'))
credit = pd.read_csv(os.path.join(caminho, 'credit_card_account.csv'))

# 2. Função de padronização Robusta
def padronizar(df, nome_conta):
    df = df.copy()
    
    # Se a coluna 'vendor' existir (caso do cartão), renomeia para 'description'
    if 'vendor' in df.columns:
        df = df.rename(columns={'vendor': 'description'})
    
    # Ajusta o sinal do valor: Débito vira Negativo
    # Note: No arquivo de cartão, 'Debit' aumenta sua dívida, no fluxo de caixa é saída.
    df['amount'] = df.apply(lambda x: x['amount'] * -1 if x['type'] == 'Debit' else x['amount'], axis=1)
    
    df['Conta'] = nome_conta
    
    # Seleciona apenas o que importa
    return df[['date', 'description', 'category', 'amount', 'Conta']]

# 3. Aplicar
df1 = padronizar(main, 'Principal')
df2 = padronizar(secondary, 'Reserva/Folha')
df3 = padronizar(credit, 'Cartão de Crédito')

# 4. Unir tudo
df_final = pd.concat([df1, df2, df3], ignore_index=True)

# 5. Tradução das Categorias (Ajustada para o que vi nos seus prints)
dicionario = {
    'Sales Revenue': 'Receita de Vendas',
    'Operating Expense': 'Despesa Operacional',
    'Payroll': 'Folha de Pagamento',
    'COGS': 'Custo de Mercadoria (CMV)',
    'Marketing': 'Marketing',
    'Utilities': 'Contas de Consumo',
    'Payment': 'Pagamento de Fatura',
    'Other': 'Outros'
}
df_final['category'] = df_final['category'].map(dicionario).fillna(df_final['category'])

# 6. Salvar o arquivo final
df_final.to_csv(os.path.join(caminho, 'Fato_Movimentacoes_Tratada.csv'), index=False, encoding='utf-8-sig')

print("Boa! Agora o arquivo 'Fato_Movimentacoes_Tratada.csv' foi gerado com sucesso.")