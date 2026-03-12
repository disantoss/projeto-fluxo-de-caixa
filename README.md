# 📊 Financial Intelligence Dashboard: Python + Power BI 🚀

![Status](https://img.shields.io/badge/Status-Finalizado-success)
![Python](https://img.shields.io/badge/Stack-Python-blue?logo=python)
![Power BI](https://img.shields.io/badge/Stack-Power_BI-yellow?logo=power-bi)

---

# 📌 Visão Geral do Projeto

Este projeto apresenta uma solução completa de **Analytics Engineering aplicada à gestão financeira de uma cafeteria**.

Para simular um cenário real de análise de dados no setor de **food service**, foram utilizados **dados públicos representando movimentações financeiras e operacionais de uma cafeteria**, incluindo receitas, custos e despesas ao longo do tempo.

O objetivo do projeto foi transformar **dados financeiros brutos** em um **dashboard analítico e estratégico**, permitindo acompanhar a saúde financeira do negócio e apoiar decisões de gestão.

A solução permite analisar indicadores como:

- Receita total
- Custos e despesas operacionais
- Lucro e margem líquida
- Fluxo de caixa mensal
- Burn Rate (taxa de queima de caixa)
- Runway (tempo estimado de sobrevivência financeira)

Esse tipo de análise é comum em empresas que precisam monitorar **sustentabilidade financeira, eficiência operacional e crescimento do negócio**.

---

# 🛠️ Pipeline de Dados

## 1️⃣ Camada de ETL & Engenharia (Python)

Antes da carga no Power BI, os dados passam por uma etapa de processamento em Python (`scripts/data_processing.py`), garantindo organização e preparação adequada para análise.

Principais etapas do pipeline:

**Consolidação de dados**  
União automática de múltiplos arquivos mensais em um único dataframe.

**Limpeza e padronização**  
Tratamento de valores nulos, padronização de tipos de dados e formatação de datas e valores monetários.

**Classificação de categorias financeiras**  
Aplicação de uma lógica de categorização para classificar as transações em:

- Receita
- CMV (Custo de Mercadoria Vendida)
- Despesas Operacionais (OpEx)
- Folha de Pagamento

Essa estrutura permite construir análises financeiras mais organizadas e facilita a modelagem dentro do Power BI.

---

# 📊 Modelagem Financeira e DRE Dinâmica (Power BI)

A etapa analítica foi desenvolvida no **Power BI**, com foco na construção de uma **Demonstração de Resultados (DRE) dinâmica**.

Para estruturar esse modelo financeiro, foram aplicadas algumas técnicas importantes de modelagem analítica:

**Tabela de Máscara (Disconnected Table)**  
Criação de uma tabela auxiliar para estruturar a DRE e permitir a exibição de subtotais financeiros que não existem diretamente na base de dados, como:

- Lucro Bruto  
- EBITDA  
- Lucro Líquido  

**DAX Avançado**  
Uso da função `SWITCH(TRUE()...)` para direcionar diferentes cálculos financeiros dependendo da linha selecionada na estrutura da DRE.

**Indicadores Financeiros Estratégicos**

O dashboard também calcula métricas importantes para análise financeira:

**Burn Rate**  
Indica a velocidade com que o caixa está sendo consumido mensalmente.

**Runway**  
Estima por quantos meses o negócio consegue operar com o caixa atual.

**Margem Líquida (%)**  
Mede a eficiência da operação em gerar lucro a partir da receita.

---

# 🎨 Design & UI/UX

O dashboard foi desenvolvido com interface **Dark Mode**, inspirada em aplicações financeiras modernas.

Principais elementos de design:

- **Backgrounds personalizados** para organização visual dos blocos de análise
- **Formatação condicional** com cores intuitivas para facilitar leitura de desempenho
- **Hierarquia visual clara**, destacando os KPIs principais do negócio

O objetivo foi criar um painel que seja **ao mesmo tempo analítico e visualmente intuitivo para tomada de decisão**.

---

# 📉 Visualização do Dashboard

<img width="1445" height="812" alt="image" src="https://github.com/user-attachments/assets/9590f433-2314-4cf9-bea1-04548eac3a9a" />

---

# 🚀 Tecnologias Utilizadas

- **Python**
- **Pandas**
- **Power BI**
- **DAX**
- **Git / GitHub**

---

# 📌 Objetivo do Projeto

Este projeto foi desenvolvido como **caso prático de engenharia e análise de dados aplicada a um cenário de negócio**, demonstrando habilidades em:

- ETL com Python
- Preparação e modelagem de dados
- Modelagem analítica no Power BI
- Construção de dashboards estratégicos
- Aplicação de conceitos financeiros em análise de dados
