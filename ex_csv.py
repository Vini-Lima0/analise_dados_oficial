
# LISTA DE EXERCÍCIOS – ANÁLISE DE DADOS COM PANDAS Dataset: Ranking
# Mundial de Universidades (notas.csv)

import pandas as pd
import matplotlib.pyplot as plt

# Carregando o dataset
df = pd.read_csv('notas.csv')

# ============================================================
# EXPLORAÇÃO INICIAL (EDA BÁSICA)
# ============================================================

# 1. Quantas linhas e colunas existem?
print("1. Linhas e colunas:", df.shape) 

# 2. Quais são os tipos de dados?
print("2. Tipos de dados:\n", df.dtypes)

# 3. Existe coluna com valores ausentes?
print("3. Colunas com valores ausentes:\n", df.isnull().any())

# 4. Qual é o período de anos disponível?
print("4. Período de anos:", df['year'].min(), "a", df['year'].max())


# 5. Quantos países diferentes existem?
print("5. Quantidade de países:", df['country'].nunique())

# ============================================================
# ESTATÍSTICAS GERAIS
# ============================================================
#=== Exercício 2 ===

# 1. Média do score
print("1. Média do score:", round(df['score'].mean(), 2))

# 2. Maior score
print("2. Maior score:", df['score'].max())

# 3. Menor score
print("3. Menor score:", df['score'].min())

# 4. Média do score por ano
print("4. Média do score por ano:\n", df.groupby('year')['score'].mean())

# 5. Desvio padrão do score
print("5. Desvio padrão do score:", round(df['score'].std(), 2))

# ============================================================
# FILTROS E SELEÇÕES
# ============================================================
#=== Exercício 3 ===
# 1. Mostre as 10 melhores universidades do mundo (menor world_rank)
top_10 = df.nsmallest(10, 'world_rank')[['institution', 'world_rank']].drop_duplicates('institution')
print("1. Top 10 mundiais:\n", top_10)

# 2. Mostre as 5 melhores universidades do Brasil (se existirem)
br_univs = df[df['country'] == 'Brazil']
top_5_br = br_univs.nsmallest(5, 'world_rank')[['institution', 'world_rank']].drop_duplicates('institution')
print("2. Top 5 Brasil:\n", top_5_br)

# 3. Mostre universidades com score maior que 90
score_90 = df[df['score'] > 90][['institution', 'score']].drop_duplicates('institution')
print("3. Score > 90:\n", score_90)

# 4. Mostre universidades dos EUA com score maior que 80
usa_80 = df[(df['country'] == 'USA') & (df['score'] > 80)][['institution', 'score']].drop_duplicates('institution')
print("4. EUA com score > 80:\n", usa_80)

# ============================================================
# SELEÇÃO AVANÇADA
# ============================================================
#=== Exercício 4 ===
# 1. Mostre apenas as colunas: institution, country e score
cols_selected = df[['institution', 'country', 'score']]
print("1. Colunas selecionadas:\n", cols_selected.head())

# 2. Mostre universidades entre rank 50 e 100
rank_50_100 = df[(df['world_rank'] >= 50) & (df['world_rank'] <= 100)][['institution', 'world_rank']]
print("2. Rank entre 50 e 100:\n", rank_50_100.head())

# 3. Mostre universidades cujo país é “United Kingdom”
uk_univs = df[df['country'] == 'United Kingdom'][['institution', 'country']]
print("3. Universidades do Reino Unido:\n", uk_univs.head())

# ============================================================ 
# MISSING VALUES
# ============================================================
#=== Exercício 5 ===
# 1. Quantos valores nulos existem na coluna broad_impact?
print("1. Nulos em broad_impact:", df['broad_impact'].isnull().sum())

# 2. Qual percentual do dataset é nulo?
perc_nulos = (df.isnull().sum().sum() / (df.shape[0] * df.shape[1])) * 100
print("2. Percentual de nulos no dataset inteiro (%):", round(perc_nulos, 2))

# 3. Remova linhas com broad_impact nulo
df_dropped = df.dropna(subset=['broad_impact'])
print("3. Linhas após remover broad_impact nulo:", df_dropped.shape[0])

# 4. Preencha valores nulos com a média
mean_before = df['broad_impact'].mean()
df_filled = df.copy()
df_filled['broad_impact'] = df_filled['broad_impact'].fillna(mean_before)

# 5. Compare a média antes e depois do preenchimento
mean_after = df_filled['broad_impact'].mean()
print(f"4 e 5. Média antes: {mean_before:.2f} | Média depois: {mean_after:.2f}")

# ============================================================ 
# GROUPBY (ANÁLISE POR PAÍS E ANO)
# ============================================================
 
# Exercício 6
# 1. Média do score por país
media_pais = df.groupby('country')['score'].mean()
print("1. Média por país:\n", media_pais.head())

# 2. País com maior média de score
pais_maior_media = df.groupby('country')['score'].mean().idxmax()
print("2. País com maior média:", pais_maior_media)

# 3. Quantidade de universidades por país
qtd_univ_pais = df.groupby('country')['institution'].nunique()
print("3. Qtd univ por país:\n", qtd_univ_pais.head())

# 4. Top 10 países com mais universidades
top_10_paises = df.groupby('country')['institution'].nunique().nlargest(10)
print("4. Top 10 países com mais univ:\n", top_10_paises)


print("\n=== Exercício 7 ===")
# 1. Média do score por ano
media_ano = df.groupby('year')['score'].mean()
print("1. Média do score por ano:\n", media_ano)

# 2. Qual ano teve maior média?
ano_maior_media = df.groupby('year')['score'].mean().idxmax()
print("2. Ano com maior média:", ano_maior_media)


# 3. Faça um gráfico da evolução do score médio ao longo do tempo
plt.figure(figsize=(10, 6))
media_ano.plot(kind='line', marker='o', color='b')
plt.title('Evolução do Score Médio por Ano', fontsize=14)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Score Médio', fontsize=12)
plt.grid(True)
plt.xticks(media_ano.index) 

# Salva o gráfico e mostra ao usuário na IDE / Jupyter (ou ambiente virtual).
plt.savefig('evolucao_score_medio.png')
