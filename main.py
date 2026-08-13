import pandas as pd
import yfinance as yf
import vectorbt as vbt

# =========================
# CONFIGURAÇÕES DO BACKTEST
# =========================

ativo = "^SPX"
media_curta = 50
media_longa = 200
capital = 10000
data_inicio = "2000-01-01"
data_fim = "2026-01-01"

# =========================
# DOWNLOAD DOS DADOS
# =========================

df = yf.download(
    ativo,
    start=data_inicio,
    end=data_fim,
    auto_adjust=False,
    progress=False
)

if df.empty:
    raise ValueError(
        "Não foi possível baixar os dados. "
        "Verifique o ticker, as datas ou a conexão com a internet."
    )

print(f"Dados baixados: {len(df)} pregões")

if isinstance(df.columns, pd.MultiIndex):
    close = df["Close"][ativo]
else:
    close = df["Close"]

close = close.dropna()

# =========================
# MÉDIAS MÓVEIS
# =========================

mm_curta = vbt.MA.run(
    close,
    window=media_curta
).ma

mm_longa = vbt.MA.run(
    close,
    window=media_longa
).ma

# =========================
# SINAIS
# =========================

entradas = mm_curta.vbt.crossed_above(mm_longa)

saidas = mm_curta.vbt.crossed_below(mm_longa)

# =========================
# BACKTEST
# =========================

portfolio = vbt.Portfolio.from_signals(
    close,
    entries=entradas,
    exits=saidas,
    init_cash=capital
)

# =========================
# RESULTADOS
# =========================

print("\n===== RESULTADOS =====")
print(f"Ativo: {ativo}")
print(f"Média curta: {media_curta}")
print(f"Média longa: {media_longa}")
print(f"Capital inicial: ${capital:,.2f}")
print(f"Capital final: ${portfolio.final_value():,.2f}")
print(f"Retorno total: {portfolio.total_return() * 100:.2f}%")
print(f"Número de operações: {portfolio.trades.count()}")

print("\n===== ESTATÍSTICAS =====")
print(portfolio.stats())
