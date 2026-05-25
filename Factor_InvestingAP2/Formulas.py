# %% Fórmula de value
import yfinance as yf
import pandas as pd
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.getLogger("yfinance").setLevel(logging.CRITICAL)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)

ACOES = [
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

def buscar_value(ticker):
    try:
        info = yf.Ticker(ticker).info
        pl        = info.get("trailingPE", 0) or 0
        pvp       = info.get("priceToBook", 0) or 0
        ev_ebitda = info.get("enterpriseToEbitda", 0) or 0
        dy        = info.get("dividendYield", 0) or 0
        componentes = [1 / v for v in [pl, pvp, ev_ebitda] if v > 0] + ([dy] if dy > 0 else [])
        value_score = sum(componentes) / len(componentes) if componentes else 0
        return {"Ação": ticker, "Value Score": round(value_score, 4)}
    except Exception:
        return None

resultado_value = []
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(buscar_value, t): t for t in ACOES}
    for future in as_completed(futures):
        res = future.result()
        if res:
            resultado_value.append(res)

df_value = pd.DataFrame(resultado_value).sort_values("Value Score", ascending=False)
print("=== TOP 10 - VALUE ===")
print(df_value.head(10).to_string(index=False))



# %% Fórmula de momentum
import yfinance as yf
import pandas as pd
import logging

logging.getLogger("yfinance").setLevel(logging.CRITICAL)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)

ACOES = [
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

try:
    dados_momentum = yf.download(ACOES, period="1y", auto_adjust=True, progress=False)["Close"]
    if dados_momentum.empty:
        print("Nenhum dado retornado pelo yfinance.")
    else:
        retornos_momentum = (
            (dados_momentum.iloc[-1] - dados_momentum.iloc[0]) / dados_momentum.iloc[0] * 100
        ).dropna().sort_values(ascending=False)
        df_momentum = pd.DataFrame({
            "Ação": retornos_momentum.index,
            "Retorno 1 ano (%)": retornos_momentum.values
        })
        print("=== TOP 10 - MOMENTUM ===")
        print(df_momentum.head(10).round(2).to_string(index=False))
except Exception as e:
    print(f"Erro ao baixar dados de momentum: {e}")



# %% Fórmula de low volatility
import yfinance as yf
import pandas as pd
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

logging.getLogger("yfinance").setLevel(logging.CRITICAL)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)

ACOES = [
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

def buscar_low_vol(ticker):
    try:
        info = yf.Ticker(ticker).info
        beta = info.get("beta", 0) or 0
        low_vol_score = 1 / beta if beta > 0 else 0
        return {"Ação": ticker, "Low Volatility Score": round(low_vol_score, 4)}
    except Exception:
        return None

resultado_low_vol = []
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(buscar_low_vol, t): t for t in ACOES}
    for future in as_completed(futures):
        res = future.result()
        if res:
            resultado_low_vol.append(res)

df_low_vol = pd.DataFrame(resultado_low_vol).sort_values("Low Volatility Score", ascending=False)
print("=== TOP 10 - LOW VOLATILITY ===")
print(df_low_vol.head(10).to_string(index=False))
