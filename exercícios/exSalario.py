import pandas as pd
df = pd.read_excel('salary.xlsx')

# 2. Linhas e Colunas
print(f"Linhas, Colunas: {df.shape}")

# 3. Média, Maior e Menor
print(f"3. Média: {df.salary.mean():.2f} | Máx: {df.salary.max()} | Mín: {df.salary.min()}")

# 4. Novo DF com colunas específicas
df_red = df[['job_title', 'salary', 'company_location', 'company_size', 'remote_ratio']]

# 5. Data Scientist: Máx/Mín e Localização
ds = df.query('job_title == "Data Scientist"')
print(f"5. Máx: {ds.salary.max()} ({ds.loc[ds.salary.idxmax(), 'company_location']}) | Mín: {ds.salary.min()} ({ds.loc[ds.salary.idxmin(), 'company_location']})")

# 6. Profissão com maior e menor média
m_job = df.groupby('job_title').salary.mean()
print(f"6. Maior: {m_job.idxmax()} | Menor: {m_job.idxmin()}")

# 7. Profissões acima da média geral
print(f"7. {m_job[m_job > df.salary.mean()].index.tolist()}")

# 8. Localização com maior média
print(f"8. {df.groupby('company_location').salary.mean().idxmax()}")

# 9. Profissões no Brasil (BR)
print(f"9. {df[df.company_location == 'BR'].job_title.unique()}")

# 10. Média salarial no Brasil
print(f"10. {df[df.company_location == 'BR'].salary.mean():.2f}")

# 11. Quantas profissões no Brasil
print(f"11. {df[df.company_location == 'BR'].job_title.nunique()}")

# 12. Profissão que mais ganha no Brasil
print(f"12. {df[df.company_location == 'BR'].sort_values('salary').job_title.iloc[-1]}")

# 13. Profissões nos US em empresas Grandes (L)
print(f"13. {df.query('company_location == \"US\" & company_size == \"L\"').job_title.nunique()}")

# 14. Média empresas médias (M) no Canadá (CA)
print(f"14. {df.query('company_location == \"CA\" & company_size == \"M\"').salary.mean():.2f}")

# 15. País com mais e menos profissões
p_counts = df.groupby('company_location').job_title.nunique()
print(f"15. Mais: {p_counts.idxmax()} | Menos: {p_counts.idxmin()}")

# 16. Quem ganha mais (Remoto/Presencial/Híbrido)
print(f"16. {df.groupby('remote_ratio').salary.mean().idxmax()}")

# 17. País com mais profissões 100% remotas
print(f"17. {df[df.remote_ratio == 100].groupby('company_location').job_title.nunique().idxmax()}")

# 16. Quem ganha mais: quem trabalha remoto, presencial ou híbrido? 
# Nota: remote_ratio geralmente é 0 (presencial), 50 (híbrido) ou 100 (remoto)
media_remoto = df.groupby('remote_ratio')['salary'].mean()
print("16. Média salarial por modalidade (0=Presencial, 50=Híbrido, 100=Remoto):\n", media_remoto)

# 17. Qual o país com maior numero de profissões trabalhando 100% remoto? 
pais_remoto = df[df['remote_ratio'] == 100].groupby('company_location')['job_title'].nunique().idxmax()
print(f"17. País com mais profissões 100% remotas: {pais_remoto}")