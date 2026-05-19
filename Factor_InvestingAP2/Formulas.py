#Fórmula de value 
import yfinance as yf
import pandas as pd

acoes = ["PETR4.SA", "BBAS3.SA", "ITUB4.SA", "BBAS3.SA", "WEGE3.SA"]
resultado = []

for ticker in acoes:
    info = yf.Ticker(ticker).info
    
    # Busca os dados de forma direta (garante zero se não existirem)
    pl        = info.get("trailingPE", 0) or 0
    pvp       = info.get("priceToBook", 0) or 0
    ev_ebitda = info.get("enterpriseToEbitda", 0) or 0
    dy        = info.get("dividendYield", 0) or 0

    # Cria a lista de componentes já invertendo os necessários em uma única linha
    componentes = [1 / v for v in [pl, pvp, ev_ebitda] if v > 0] + [dy]
    
    # Calcula a média do Score
    value_score = sum(componentes) / len(componentes) if componentes else 0
    
    resultado.append({"Ação": ticker, "Value Score": round(value_score, 4)})

# Transforma em tabela, ordena do maior para o menor e exibe tudo
df = pd.DataFrame(resultado).sort_values("Value Score", ascending=False)
print(df.to_string(index=False))


#Fórmula de momentum
import yfinance as yf

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

for acao in acoes:

    try:

        dados = yf.Ticker(acao).history(period="1y")

        preco_inicial = dados["Close"].iloc[0]
        preco_final = dados["Close"].iloc[-1]

        momentum = ((preco_final - preco_inicial) / preco_inicial) * 100

        print(f"{acao} --> {round(momentum, 2)}%")

    except:

        print(f"Erro em {acao}")



resultado = []

for acao in acoes:

    try:

        dados = yf.Ticker(acao).history(period="1y")

        preco_inicial = dados["Close"].iloc[0]
        preco_final = dados["Close"].iloc[-1]

        momentum = ((preco_final - preco_inicial) / preco_inicial) * 100

        resultado.append((acao, round(momentum, 2)))

    except:

        pass


resultado.sort(key=lambda x: x[1], reverse=True)

top_10 = resultado[:10]

for acao, momentum in top_10:

    print(f"{acao} --> {momentum}%")   



#Fórmula de low volatility
import yfinance as yf
import pandas as pd
acoes = ["PETR4.SA", "BBAS3.SA", "ITUB4.SA", "BBAS3.SA", "WEGE3.SA"]
resultado = []

for ticker in acoes:
    info = yf.Ticker(ticker).info
    
    # Busca os dados de forma direta (garante zero se não existirem)
    beta = info.get("beta", 0) or 0

    # O score é o inverso do beta
    low_vol_score = 1 / beta if beta > 0 else 0
    
    resultado.append({"Ação": ticker, "Low Volatility Score": round(low_vol_score, 4)})

# Transforma em tabela, ordena do maior para o menor e exibe tudo    
df = pd.DataFrame(resultado).sort_values("Low Volatility Score", ascending=False)
print(df.to_string(index=False))