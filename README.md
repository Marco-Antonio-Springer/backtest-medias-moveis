# Backtest de Estratégia com Médias Móveis

Projeto em Python para testar uma estratégia de investimento baseada no cruzamento de médias móveis utilizando dados históricos.

## Objetivo

O objetivo deste projeto é transformar uma estratégia simples de análise técnica em um processo sistemático de backtesting, permitindo avaliar como ela teria se comportado em dados históricos.

O projeto também foi desenvolvido como prática de:

- Python aplicado ao mercado financeiro;
- manipulação de dados com Pandas;
- obtenção de dados financeiros com yfinance;
- backtesting com VectorBT;
- organização de projetos no GitHub.

## Estratégia

A estratégia utiliza duas médias móveis:

- Média móvel curta: 50 períodos;
- Média móvel longa: 200 períodos.

São gerados os seguintes sinais:

- Compra: quando a média móvel curta cruza para cima da média móvel longa;
- Venda: quando a média móvel curta cruza para baixo da média móvel longa.

O backtest começa com um capital inicial de US$ 10.000.

## Dados

Os dados históricos são obtidos por meio do yfinance.

Configuração utilizada na versão 1.0:

- Ativo: S&P 500 (^SPX);
- Período: 01/01/2000 a 01/01/2026;
- Média curta: 50 períodos;
- Média longa: 200 períodos;
- Capital inicial: US$ 10.000.

## Tecnologias utilizadas

- Python
- Pandas
- yfinance
- VectorBT
- Matplotlib
- Git/GitHub

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/Marco-Antonio-Springer/backtest-medias-moveis.git
cd backtest-medias-moveis

Projeto desenvolvido para fins educacionais somente.
