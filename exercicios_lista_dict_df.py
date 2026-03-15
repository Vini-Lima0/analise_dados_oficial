"""
Aula - Exercicios de Pandas DataFrame
Como usar:
1) Leia o enunciado de cada bloco.
2) Complete o codigo onde estiver RESOLUCAO.
3) Rode o arquivo e valide os resultados.

Requisito:
- Instalar pandas: pip install pandas
"""

import pandas as pd

print("="*50)
print("INICIANDO BLOCOS DE VENDAS")
print("="*50)

# -------------------------------------------------
# BLOCO 1: criar DataFrame e inspecionar estrutura
# -------------------------------------------------
dados_vendas = {
    "mes": ["Jan", "Jan", "Fev", "Fev", "Mar", "Mar"],
    "filial": ["Centro", "Norte", "Centro", "Norte", "Centro", "Norte"],
    "vendas": [12000, 9500, 13500, 10200, 14100, 11000],
    "clientes": [210, 180, 225, 190, 235, 205],
}

# Exercicio 1:
print("\n--- BLOCO 1 ---")
# a) Crie o DataFrame df_vendas usando dados_vendas
df_vendas = pd.DataFrame(dados_vendas)
print("DataFrame criado:\n", df_vendas)

# b) Mostre as 5 primeiras linhas
print("5 primeiras linhas:\n", df_vendas.head())

# c) Mostre o formato (linhas, colunas)
print("\nFormato (linhas, colunas):", df_vendas.shape)

# d) Mostre os tipos de dados das colunas
print("\nTipos de dados:\n", df_vendas.dtypes)


# -------------------------------------------------
# BLOCO 2: selecionar colunas e linhas
# -------------------------------------------------
print("\n--- BLOCO 2 ---")
# Exercicio 2:
# a) Mostre apenas as colunas "mes" e "vendas"
print("Colunas 'mes' e 'vendas':\n", df_vendas[["mes", "vendas"]])

# b) Mostre somente a primeira linha
print("\nPrimeira linha:\n", df_vendas.iloc[0])

# c) Mostre as linhas de indice 2 ate 4
print("\nLinhas de indice 2 a 4:\n", df_vendas.iloc[2:5])


# -------------------------------------------------
# BLOCO 3: filtros com condicoes de negocio
# -------------------------------------------------
print("\n--- BLOCO 3 ---")
# Exercicio 3:
# a) Filtre vendas acima de 12000
print("Vendas > 12000:\n", df_vendas[df_vendas["vendas"] > 12000])

# b) Filtre apenas a filial "Centro"
print("\nApenas filial Centro:\n", df_vendas[df_vendas["filial"] == "Centro"])

# c) Filtre vendas acima de 11000 na filial "Norte"
filtro_c = (df_vendas["vendas"] > 11000) & (df_vendas["filial"] == "Norte")
print("\nVendas > 11000 na filial Norte:\n", df_vendas[filtro_c]) # Resultado será vazio neste dataset


# -------------------------------------------------
# BLOCO 4: novas colunas e metricas
# -------------------------------------------------
print("\n--- BLOCO 4 ---")
# Exercicio 4:
# a) Crie a coluna "ticket_medio" = vendas / clientes
df_vendas["ticket_medio"] = df_vendas["vendas"] / df_vendas["clientes"]

# b) Crie a coluna "meta_batida" com True para vendas >= 13000
df_vendas["meta_batida"] = df_vendas["vendas"] >= 13000

# c) Mostre apenas "filial", "mes", "ticket_medio", "meta_batida"
print("Novas colunas e métricas:\n", df_vendas[["filial", "mes", "ticket_medio", "meta_batida"]])


# -------------------------------------------------
# BLOCO 5: agregacao com groupby
# -------------------------------------------------
print("\n--- BLOCO 5 ---")
# Exercicio 5:
# a) Calcule total de vendas por filial
print("Total de vendas por filial:\n", df_vendas.groupby("filial")["vendas"].sum())

# b) Calcule media de clientes por mes
print("\nMédia de clientes por mês:\n", df_vendas.groupby("mes")["clientes"].mean())

# c) Descubra a filial com maior total de vendas
filial_maior_venda = df_vendas.groupby("filial")["vendas"].sum().idxmax()
print("\nFilial com maior total de vendas:", filial_maior_venda)


# -------------------------------------------------
# BLOCO 6: ordenacao e ranking
# -------------------------------------------------
print("\n--- BLOCO 6 ---")
# Exercicio 6:
# a) Ordene df_vendas por "vendas" em ordem decrescente
df_vendas = df_vendas.sort_values(by="vendas", ascending=False)

# b) Pegue os 3 maiores resultados de vendas
print("Top 3 maiores vendas:\n", df_vendas.head(3))

# c) Mostre um ranking com "filial", "mes", "vendas"
print("\nRanking de vendas:\n", df_vendas[["filial", "mes", "vendas"]])


# -------------------------------------------------
# BLOCO 7: desafio final de analise
# -------------------------------------------------
print("\n--- BLOCO 7 ---")
# Exercicio 7 (desafio):
# 1) Gere um resumo por filial com: total_vendas, media_ticket_medio, total_clientes
resumo_filial = df_vendas.groupby("filial").agg(
    total_vendas=("vendas", "sum"),
    media_ticket_medio=("ticket_medio", "mean"),
    total_clientes=("clientes", "sum")
)

# 2) Ordene o resumo por total_vendas (desc)
resumo_filial = resumo_filial.sort_values(by="total_vendas", ascending=False)
print("Resumo por filial:\n", resumo_filial)

# 3) Exiba qual filial teve melhor desempenho geral
melhor_filial = resumo_filial.index[0]
print("\nFilial com melhor desempenho geral:", melhor_filial)




print("\n\n" + "="*50)
print("PARTE 1 – Estrutura lista + dicionário")
print("="*50)

dados_list_dict = [{
    "Column A": [1, 2, 3],
    "Column B": [4, 5, 6],
    "Column C": [7, 8, 9]
}]

# -----------------------------------------------------------
# EXERCÍCIO 1 – Explorando a estrutura
# -----------------------------------------------------------
print("\n--- EXERCÍCIO 1 ---")
# 1. Qual é o tipo de dados_list_dict? -> list
print("1. Tipo de dados_list_dict:", type(dados_list_dict))
# 2. Qual é o tipo do primeiro elemento? -> dict
print("2. Tipo do primeiro elemento:", type(dados_list_dict[0]))
# 3. Como acessar a lista da "Column A"?
print("3. Lista da Column A:", dados_list_dict[0]["Column A"])
# 4. Como acessar o segundo elemento da "Column C"?
print("4. Segundo elemento da Column C:", dados_list_dict[0]["Column C"][1])


# -----------------------------------------------------------
# EXERCÍCIO 2 – Convertendo para DataFrame
# -----------------------------------------------------------
print("\n--- EXERCÍCIO 2 ---")
# 1. Converta dados_list_dict[0] em um DataFrame chamado df1
df1 = pd.DataFrame(dados_list_dict[0])

# 2. Mostre shape e tipos das colunas
print("Shape:", df1.shape)
print("Tipos das colunas:\n", df1.dtypes)

# 3. Calcule soma e média de cada coluna
print("\nSoma de cada coluna:\n", df1.sum())
print("\nMédia de cada coluna:\n", df1.mean())


# -----------------------------------------------------------
# EXERCÍCIO 3 – Criando novas colunas
# -----------------------------------------------------------
print("\n--- EXERCÍCIO 3 ---")
# 1. Crie coluna "Total" = soma das colunas
df1["Total"] = df1[["Column A", "Column B", "Column C"]].sum(axis=1)

# 2. Crie coluna "Media" = média por linha
df1["Media"] = df1[["Column A", "Column B", "Column C"]].mean(axis=1)

# 3. Filtre linhas onde Total > 10
print("Linhas onde Total > 10:\n", df1[df1["Total"] > 10])


# -----------------------------------------------------------
# EXERCÍCIO 4 – Conversões estruturais
# -----------------------------------------------------------
print("\n--- EXERCÍCIO 4 ---")
# 1. Converta df1 para lista de dicionários
df1_records = df1.to_dict(orient="records")
print("Lista de dicionários (records):\n", df1_records)

# Converta df1 para dicionário de listas
df1_list = df1.to_dict(orient="list")
print("\nDicionário de listas (list):\n", df1_list)


# -----------------------------------------------------------
# EXERCÍCIO 5 – Trabalhando com lista
# -----------------------------------------------------------
print("\n--- EXERCÍCIO 5 ---")
# 1. Transforme a coluna "Column A" em uma lista
lista_a = df1["Column A"].tolist()

# 2. Multiplique cada elemento da lista por 10
lista_a_x10 = [valor * 10 for valor in lista_a]

# 3. Crie uma nova coluna
df1["Column A x10"] = lista_a_x10
print("DataFrame com a nova coluna:\n", df1)




print("\n\n" + "="*50)
print("BASE DE DADOS - EXPORTAÇÃO")
print("="*50)

dados = [
    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 5000},
    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 3000},
    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 4000},
    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 6000},
    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-03", "valor": 7000},
]

# ===========================================================
# PARTE 1 – EXPLORAÇÃO INICIAL
# ===========================================================
print("\n--- EXERCÍCIO 1 ---")
# 1. Qual o tipo da variável dados? -> list
print("1. Tipo da variável:", type(dados))
# 2. Quantos registros existem?
print("2. Quantidade de registros:", len(dados))
# 3. Quais são as chaves do primeiro dicionário?
print("3. Chaves do primeiro dicionário:", list(dados[0].keys()))
# 4. Liste todos os países existentes (sem repetição).
paises_unicos = set(d["nome_pais"] for d in dados)
print("4. Países únicos:", paises_unicos)


# ===========================================================
# PARTE 2 – CONVERSÃO PARA DATAFRAME
# ===========================================================
print("\n--- EXERCÍCIO 2 ---")
# 1. Converta dados para DataFrame chamado df
df = pd.DataFrame(dados)

# 2. Mostre shape, tipos e primeiras linhas
print("Shape:", df.shape)
print("\nTipos das colunas:\n", df.dtypes)
print("\nPrimeiras linhas:\n", df.head())

# 3. Converta a coluna periodo para datetime
df["periodo"] = pd.to_datetime(df["periodo"])
print("\nTipo do 'periodo' após conversão:", df["periodo"].dtype)


# ===========================================================
# PARTE 3 – FILTROS E ORDENAÇÃO
# ===========================================================
print("\n--- EXERCÍCIO 3 ---")
# 1. Filtre apenas Brasil
print("Apenas Brasil:\n", df[df["nome_pais"] == "Brasil"])

# 2. Filtre apenas Produto A
print("\nApenas Produto A:\n", df[df["descricao"] == "Produto A"])

# 3. Filtre valor > 4000
print("\nValor > 4000:\n", df[df["valor"] > 4000])

# 4. Combine Brasil + Produto A
print("\nBrasil e Produto A:\n", df[(df["nome_pais"] == "Brasil") & (df["descricao"] == "Produto A")])


print("\n--- EXERCÍCIO 4 ---")
# 1. Ordene por valor crescente
print("Valor crescente:\n", df.sort_values(by="valor", ascending=True))

# 2. Ordene por valor decrescente
print("\nValor decrescente:\n", df.sort_values(by="valor", ascending=False))

# 3. Ordene por periodo e depois por valor
print("\nOrdenado por periodo e valor:\n", df.sort_values(by=["periodo", "valor"]))


# ===========================================================
# PARTE 4 – AGREGAÇÕES
# ===========================================================
print("\n--- EXERCÍCIO 5 ---")
# 1. Total exportado por país
print("Total por país:\n", df.groupby("nome_pais")["valor"].sum())

# 2. Total exportado por produto
print("\nTotal por produto:\n", df.groupby("descricao")["valor"].sum())

# 3. Média por país
print("\nMédia por país:\n", df.groupby("nome_pais")["valor"].mean())

# 4. Quantidade de operações por país
print("\nQuantidade de operações por país:\n", df.groupby("nome_pais")["valor"].count())


print("\n--- EXERCÍCIO 6 ---")
# Agrupe por nome_pais e descricao. Calcule soma, média e contagem
resumo_pais_produto = df.groupby(["nome_pais", "descricao"])["valor"].agg(["sum", "mean", "count"])
print("GroupBy Múltiplo:\n", resumo_pais_produto)

# Explique em comentário o que essa tabela representa
# RESPOSTA: Essa tabela representa um detalhamento do desempenho das exportações. 
# Ela mostra, para cada país, quanto gerou cada produto (soma), a média de valor por operação (mean) e quantas vezes aquele produto foi exportado (count).


# ===========================================================
# PARTE 5 – PIVOT TABLE
# ===========================================================
print("\n--- EXERCÍCIO 7 ---")
# Pivot por Produto
pivot_produto = df.pivot_table(index="periodo", columns="descricao", values="valor", aggfunc="sum")
print("Pivot Table (Produto):\n", pivot_produto)

# Responda:
print("\nRespostas:")
print("1. Qual produto vendeu mais? -> Produto A (Total de 16000)")
print("2. Qual mês teve maior valor total? -> 2023-02 (Fevereiro - Total de 10000)")
print("3. Existe mês sem venda? -> Sim, o Produto B não teve vendas (aparece como NaN) em Março de 2023.")


print("\n--- EXERCÍCIO 8 ---")
# Pivot por País
pivot_pais = df.pivot_table(index="periodo", columns="nome_pais", values="valor", aggfunc="sum")
print("Pivot Table (País):\n", pivot_pais)

# Explique o que podemos interpretar dessa tabela
# RESPOSTA: A tabela demonstra o fluxo histórico das exportações segmentado geograficamente.
# Podemos ver que o Brasil exportou em Janeiro e Março (ficando ausente em Fev), enquanto a Argentina exportou exclusivamente no mês de Fevereiro.


# ===========================================================
# PARTE 6 – FEATURE ENGINEERING
# ===========================================================
print("\n--- EXERCÍCIO 9 ---")
# 1. Extraia ano e mês da coluna periodo
df["ano"] = df["periodo"].dt.year
df["mes"] = df["periodo"].dt.month

# 2. Crie coluna valor_mil (valor / 1000)
df["valor_mil"] = df["valor"] / 1000

# 3. Calcule crescimento percentual por produto mês a mês
# Ordenamos por período antes para garantir a ordem cronológica correta
df = df.sort_values(by="periodo")
df["crescimento_pct"] = df.groupby("descricao")["valor"].pct_change() * 100

print("Feature Engineering aplicadas:\n", df[["periodo", "descricao", "valor", "ano", "mes", "valor_mil", "crescimento_pct"]])


# ===========================================================
# PARTE 7 – QUALIDADE DE DADOS
# ===========================================================
print("\n--- EXERCÍCIO 10 ---")
# 1. Verifique valores nulos
print("Valores Nulos:\n", df.isnull().sum())

# 2. Verifique valores negativos
valores_negativos = df[df["valor"] < 0]
print("\nValores Negativos:\n", valores_negativos if not valores_negativos.empty else "Nenhum valor negativo encontrado.")

# 3. Verifique duplicatas
print("\nDuplicatas (linhas idênticas):", df.duplicated().sum())








