# 📊 Financial Intelligence Dashboard: Python + Power BI 🚀

![Status](https://img.shields.io/badge/Status-Finalizado-success)
![Python](https://img.shields.io/badge/Stack-Python-blue?logo=python)
![Power BI](https://img.shields.io/badge/Stack-Power_BI-yellow?logo=power-bi)

## 📌 Visão Geral do Projeto
Este projeto entrega uma solução completa de **Analytics Engineering** aplicada ao setor financeiro. O objetivo foi transformar dados brutos de movimentações bancárias e contábeis em um dashboard estratégico de alto nível (Dark Mode), focado no monitoramento de saúde de caixa, lucratividade e indicadores de crescimento.

---

## 🛠️ O Diferencial Técnico: Pipeline de Dados

### 1. Camada de ETL & Engenharia (Python)
Diferente de modelos simples, os dados aqui passam por um tratamento prévio em Python (`scripts/data_processing.py`), garantindo escalabilidade:
* **Consolidação Automática:** União de múltiplos arquivos mensais em um dataframe único.
* **Limpeza e Padronização:** Tratamento de nulos, tipagem de moedas e datas.
* **Classificação de Categorias:** Algoritmo simples de mapeamento para categorizar transações (Receita, CMV, OpEx, Folha) antes da carga no BI.

### 2. Modelagem e DRE Estruturada (Power BI)
A parte mais complexa do projeto foi a criação da **DRE (Demonstração de Resultados) Dinâmica**:
* **Tabela de Máscara (Disconnected Table):** Criação de um gabarito de estrutura para permitir linhas de subtotal (Ex: Lucro Bruto, EBITDA) que não existem na base original.
* **DAX Avançado:** Uso intenso da função `SWITCH(TRUE()...)` para direcionar cálculos específicos conforme a linha da DRE selecionada.
* **Indicadores Críticos:** * **Burn Rate:** Monitoramento de queima de caixa mensal.
  * **Runway:** Cálculo de pista de sobrevivência (meses de caixa restantes).
  * **Margem Líquida %:** Eficiência do lucro sobre a receita bruta.

---

## 🎨 Design & UI/UX
O dashboard foi desenvolvido com uma interface **Dark Mode**, inspirada em sistemas financeiros modernos da Apple e Nubank, utilizando:
* **Backgrounds Personalizados:** Criados para delimitar espaços e evitar poluição visual.
* **Formatação Condicional:** Cores neon (Verde/Ciano para lucro, Vermelho/Rosa para prejuízo) para leitura imediata da performance.
* **Hierarquia Visual:** Cards transparentes integrados ao design para foco nos KPIs principais.

---

## 📉 Visualização do Dashboard
<img width="1448" height="813" alt="image" src="https://github.com/user-attachments/assets/e860bb8f-f642-4a70-81f4-e3a8b54d334f" />

