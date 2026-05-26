# =============================================================================
# FACTOR INVESTING — ANÁLISE DE AÇÕES DA B3
# =============================================================================
# Factor investing é uma estratégia que seleciona ações com base em
# características (fatores) que historicamente geram retornos superiores.
# Aqui usamos 3 fatores: Value, Momentum e Low Volatility.
# =============================================================================

import yfinance as yf
import pandas as pd
import numpy as np
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.getLogger("yfinance").setLevel(logging.CRITICAL)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)

# Lista de ações analisadas (principais ações da B3)
acoes = [
    "ABEV3.SA","ALOS3.SA","ASAI3.SA","AZUL4.SA","B3SA3.SA",
    "BBAS3.SA","BBDC3.SA","BBDC4.SA","BBSE3.SA","BPAC11.SA",
    "BRAP4.SA","BRFS3.SA","BRKM5.SA","CCRO3.SA","CMIG4.SA",
    "CMIN3.SA","COGN3.SA","CPFE3.SA","CPLE6.SA","CRFB3.SA",
    "CSAN3.SA","CSNA3.SA","CVCB3.SA","CYRE3.SA","DXCO3.SA",
    "EGIE3.SA","ELET3.SA","ELET6.SA","EMBR3.SA","ENEV3.SA",
    "ENGI11.SA","EQTL3.SA","EZTC3.SA","FLRY3.SA","GGBR4.SA",
    "GOAU4.SA","GOLL4.SA","HAPV3.SA","HYPE3.SA","IGTI11.SA",
    "IRBR3.SA","ITSA4.SA","ITUB4.SA","JBSS3.SA","KLBN11.SA",
    "LREN3.SA","MGLU3.SA","MRFG3.SA","MRVE3.SA","MULT3.SA",
    "NTCO3.SA","PCAR3.SA","PETR3.SA","PETR4.SA","PETZ3.SA",
    "PRIO3.SA","PSSA3.SA","RADL3.SA","RAIL3.SA","RDOR3.SA",
    "RECV3.SA","RENT3.SA","SANB11.SA","SBSP3.SA","SLCE3.SA",
    "SMTO3.SA","SUZB3.SA","TAEE11.SA","TIMS3.SA","TOTS3.SA",
    "UGPA3.SA","USIM5.SA","VALE3.SA","VAMO3.SA","VBBR3.SA",
    "VIIA3.SA","VIVT3.SA","WEGE3.SA","YDUQ3.SA","ARZZ3.SA",
    "BEEF3.SA","BRPR3.SA","CASH3.SA","CIEL3.SA","CSMG3.SA",
    "ECOR3.SA","GMAT3.SA","GUAR3.SA","HBOR3.SA","JHSF3.SA",
    "KEPL3.SA","LWSA3.SA","MDIA3.SA","MOVI3.SA","ODPV3.SA",
    "POSI3.SA","SAPR11.SA","TRPL4.SA","UNIP6.SA","VVEO3.SA"
]


# %% ─── FATOR 1: VALUE ────────────────────────────────────────────────────────
# Ideia: comprar ações "baratas" em relação ao seu valor real.
# Usamos 4 indicadores fundamentalistas:
#   P/L  (Preço / Lucro)            → quanto o mercado paga por R$1 de lucro
#   P/VP (Preço / Valor Patrimonial) → quanto paga por R$1 de patrimônio
#   EV/EBITDA                        → valor da empresa vs. lucro operacional
#   Dividend Yield                   → % de dividendos pagos ao investidor
# Quanto MENOR o P/L, P/VP e EV/EBITDA → mais barata a ação (melhor para value)
# Quanto MAIOR o Dividend Yield → mais atrativa
# O Value Score combina tudo isso: maior score = ação mais barata/atrativa

def buscar_value(ticker):
    try:
        info      = yf.Ticker(ticker).info
        pl        = info.get("trailingPE", 0) or 0        # Preço / Lucro
        pvp       = info.get("priceToBook", 0) or 0       # Preço / Valor Patrimonial
        ev_ebitda = info.get("enterpriseToEbitda", 0) or 0 # EV / EBITDA
        dy        = info.get("dividendYield", 0) or 0     # Dividend Yield

        # Inverte P/L, P/VP e EV/EBITDA (menor = melhor → maior score)
        componentes = [1 / v for v in [pl, pvp, ev_ebitda] if v > 0] + ([dy] if dy > 0 else [])
        value_score = sum(componentes) / len(componentes) if componentes else 0
        return {"Ação": ticker, "Value Score": round(value_score, 4)}
    except:
        print(f"Erro em {ticker}")
        return None

resultado = []
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(buscar_value, t): t for t in acoes}
    for future in as_completed(futures):
        res = future.result()
        if res:
            resultado.append(res)

df = pd.DataFrame(resultado).sort_values("Value Score", ascending=False)
print("─── TOP 10 VALUE (ações mais baratas) ───")
print(df.head(10).to_string(index=False))
top_value = df.head(10)["Ação"].tolist()


# %% ─── FATOR 2: MOMENTUM ─────────────────────────────────────────────────────
# Ideia: ações que subiram no último ano tendem a continuar subindo.
# Simplesmente medimos o retorno total de cada ação nos últimos 12 meses.
# Maior retorno = maior momentum = melhor posição no ranking.

dados = yf.download(acoes, period="1y", auto_adjust=True, progress=False)["Close"]

# Retorno = (preço final - preço inicial) / preço inicial × 100
retornos = ((dados.iloc[-1] - dados.iloc[0]) / dados.iloc[0] * 100).dropna().sort_values(ascending=False)

df = pd.DataFrame({"Ação": retornos.index, "Momentum (%)": retornos.round(2).values})
print("\n─── TOP 10 MOMENTUM (maiores altas em 12 meses) ───")
print(df.head(10).to_string(index=False))
top_momentum = df.head(10)["Ação"].tolist()


# %% ─── FATOR 3: LOW VOLATILITY ───────────────────────────────────────────────
# Ideia: ações que oscilam menos tendem a ter melhor retorno ajustado ao risco.
# Usamos o Beta como medida de volatilidade:
#   Beta = 1  → a ação oscila igual ao mercado (IBOV)
#   Beta < 1  → oscila MENOS que o mercado (menos arriscada)
#   Beta > 1  → oscila MAIS que o mercado (mais arriscada)
# O Low Volatility Score é 1/Beta: menor Beta → maior score → melhor posição

def buscar_low_vol(ticker):
    try:
        info = yf.Ticker(ticker).info
        beta = info.get("beta", 0) or 0
        low_vol_score = 1 / beta if beta > 0 else 0  # inverte: menor beta = maior score
        return {"Ação": ticker, "Low Volatility Score": round(low_vol_score, 4)}
    except:
        print(f"Erro em {ticker}")
        return None

resultado = []
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(buscar_low_vol, t): t for t in acoes}
    for future in as_completed(futures):
        res = future.result()
        if res:
            resultado.append(res)

df = pd.DataFrame(resultado).sort_values("Low Volatility Score", ascending=False)
print("\n─── TOP 10 LOW VOLATILITY (ações menos voláteis) ───")
print(df.head(10).to_string(index=False))
top_low_vol = df.head(10)["Ação"].tolist()


# %% ─── BACKTEST DO PORTFÓLIO MULTIFATOR ─────────────────────────────────────
# Unimos as top 10 de cada fator para formar o portfólio final.
# Backtest = simular como teria sido investir nessas ações no passado.
# Estratégia: Equal Weight (mesmo valor investido em cada ação), sem rebalanceamento.
# Benchmark: IBOV (índice que representa o mercado brasileiro).
# Taxa livre de risco: Selic (~10,75% a.a.) — o mínimo que um investidor esperaria ganhar.

# Portfólio = união das top 10 de cada fator (pode ter menos de 30 se houver sobreposição)
portfolio = list(set(top_value + top_momentum + top_low_vol))
print(f"\n─── PORTFÓLIO MULTIFATOR: {len(portfolio)} ações ───")
print(sorted(portfolio))

# Baixa preços históricos dos últimos 5 anos
# Remove ações com menos de 60% dos dados disponíveis (ex: IPOs recentes)
precos = yf.download(portfolio, period="5y", auto_adjust=True, progress=False)["Close"]
precos = precos.dropna(axis=1, thresh=int(len(precos) * 0.6))

# Retorno diário de cada ação → média = retorno do portfólio (equal weight)
retornos_diarios = precos.pct_change().dropna(how="all")
portfolio_ret = retornos_diarios.mean(axis=1)

# Baixa retorno diário do IBOV para comparação
ibov = yf.download("^BVSP", period="5y", auto_adjust=True, progress=False)["Close"]
ibov_ret = ibov.pct_change().dropna().squeeze()

# Alinha as datas (garante que portfólio e IBOV tenham os mesmos dias)
idx = portfolio_ret.index.intersection(ibov_ret.index)
portfolio_ret = portfolio_ret.loc[idx]
ibov_ret = ibov_ret.loc[idx]

rf_anual  = 0.1075       # Selic ~10,75% ao ano
rf_diaria = rf_anual / 252  # 252 dias úteis por ano

# ── Métricas de desempenho ──────────────────────────────────────────────────

# Retorno total e anualizado (CAGR)
retorno_total      = (1 + portfolio_ret).prod() - 1
n_anos             = len(portfolio_ret) / 252
retorno_anualizado = (1 + retorno_total) ** (1 / n_anos) - 1

# Volatilidade: mede o quanto o portfólio oscilou (desvio padrão anualizado)
volatilidade = portfolio_ret.std() * np.sqrt(252)

# Sharpe Ratio: retorno extra (acima da Selic) por unidade de risco total
# > 1 = bom | > 2 = muito bom | negativo = não compensou o risco vs. Selic
sharpe = (retorno_anualizado - rf_anual) / volatilidade

# Sortino Ratio: igual ao Sharpe, mas considera só a volatilidade de queda
# Penaliza menos as altas e mais as baixas — mais justo para o investidor
retornos_negativos = portfolio_ret[portfolio_ret < rf_diaria]
downside = retornos_negativos.std() * np.sqrt(252) if len(retornos_negativos) > 0 else 0
sortino  = (retorno_anualizado - rf_anual) / downside if downside > 0 else 0

# Max Drawdown: maior queda do pico ao fundo durante o período
# Ex: -25% significa que em algum momento o portfólio caiu 25% do seu topo
cum_ret      = (1 + portfolio_ret).cumprod()
max_drawdown = ((cum_ret - cum_ret.cummax()) / cum_ret.cummax()).min()

# Beta: sensibilidade do portfólio em relação ao IBOV
# Beta > 1 → cai/sobe mais que o mercado | Beta < 1 → cai/sobe menos
cov_matrix    = np.cov(portfolio_ret.values, ibov_ret.values)
beta          = cov_matrix[0, 1] / cov_matrix[1, 1]

# Alpha: retorno extra gerado ALÉM do que o Beta já explicaria
# Alpha positivo = o portfólio superou o mercado, ajustado pelo risco
ibov_ret_anual = (1 + ibov_ret).prod() ** (252 / len(ibov_ret)) - 1
alpha = retorno_anualizado - (rf_anual + beta * (ibov_ret_anual - rf_anual))

# ── Resultado final ─────────────────────────────────────────────────────────
print(f"\n{'='*45}")
print(f"   BACKTEST — PORTFÓLIO MULTIFATOR")
print(f"{'='*45}")
print(f" Período:              {precos.index[0].date()} → {precos.index[-1].date()} ({n_anos:.1f} anos)")
print(f" Nº de ações:          {len(precos.columns)}")
print(f"{'─'*45}")
print(f" Retorno Total:        {retorno_total*100:.2f}%")
print(f" Retorno Anualizado:   {retorno_anualizado*100:.2f}%  (ao ano)")
print(f" Volatilidade (a.a.):  {volatilidade*100:.2f}%  (oscilação média)")
print(f"{'─'*45}")
print(f" Sharpe Ratio:         {sharpe:.4f}  (retorno/risco total)")
print(f" Sortino Ratio:        {sortino:.4f}  (retorno/risco de queda)")
print(f"{'─'*45}")
print(f" Max Drawdown:         {max_drawdown*100:.2f}%  (maior queda do período)")
print(f"{'─'*45}")
print(f" Beta vs IBOV:         {beta:.4f}  (sensibilidade ao mercado)")
print(f" Alpha (a.a.):         {alpha*100:.2f}%  (retorno acima do esperado)")
print(f"{'='*45}")
