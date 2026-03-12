#1
aluno = {
    "nome" : "Vinicius",
    'idade' : 18, 
    'curso' : 'Administração'
}
print({aluno["nome"]})
print({aluno['idade']})
print([aluno['curso']])

#2
produto = {
    "nome": "Teclado Mecânico",
    "preco": 350.00,
    "estoque": 10
}
produto["marca"] = "Razer"
produto["preco"] = 320.00
produto["estoque"] -= 2
del produto["marca"]
print("O dicionário atualizado é:")
print(produto)

#3
notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8
}
print("Nota individual por aluno")
for aluno, nota in notas.items():
    print(f"Aluno(a): {aluno}, Nota: {nota}")
    media_das_notas = sum(notas.values()) / len(notas)
print("A média geral da turma é:", media_das_notas)

#4
numeros = {"a": 10, "b": 20, "c": 30}
print("A soma de todos os números é:", sum(numeros.values()))

#5
lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
frequencia = {}
for item in lista:
    if item in frequencia:
        frequencia[item] += 1
    else:
        frequencia[item] = 1
print("A frequência de cada item é:", frequencia)

#6
produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
novo_dict = {}
for prod, preco in produtos.items():
    if preco > 50:
        novo_dict[prod] = preco
print(novo_dict)

#7 
tradutor = {"dog": "cachorro", "pig": "porco", "book": "livro"}
palavra =input("Digite um palavra em ingles:").lower()
if palavra in tradutor:
    print("A tradução é:", tradutor[palavra])
else:
    print("Palavra não encontrada")


#7
tradutor = {
    "door": "porta",
    "cat": "gato",
    "dog": "cachorro"
}
palavra = input("Digite a palavra em ingles").lower()
if palavra in tradutor:
    print(f"Traduçao: {tradutor[palavra]}")
else:
    print("Palavra nao encontrada")

#8 
Lista_de_compras = {}
produto = input("Digite o produto")
Quantidade = int(input("Digite a quantidade"))
if produto in Lista_de_compras:
        Lista_de_compras[produto] = Lista_de_compras[produto] + Quantidade
else:
    Lista_de_compras[produto] = Quantidade  
print(Lista_de_compras) 

#9
turma = {
    "Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}
T2 = {}

turma["Enrico"] = {"idade": 18, "notas": [5,7,9]}
print(turma)

for K,V in turma.items():
    md = sum(V["notas"])/len(V["notas"])
    print(f"{K}: Media {md}")
    T2[K] = md

mx = max(T2.values())
print(f"a maior media foi {mx}")

#10
funcionarios = {}

for i in range(3):  # vai cadastrar 3 funcionários como exemplo
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    salario = float(input("Salário: "))

    funcionarios[nome] = {"Cargo": cargo, "Salário": salario}


nome_consulta = input("\nDigite o nome do funcionário para consultar: ")
if nome_consulta in funcionarios:
    print(f"Nome: {nome_consulta}")
    print(f"Cargo: {funcionarios[nome_consulta]['Cargo']}")
    print(f"Salário: R$ {funcionarios[nome_consulta]['Salário']:.2f}")
else:
    print("Funcionário não encontrado.")

# Exercício 11 – Faturamento diário
faturamento = [
    {"dia": "segunda", "valor": 1200},
    {"dia": "terça", "valor": 1500},
    {"dia": "quarta", "valor": 900},
    {"dia": "quinta", "valor": 1800},
    {"dia": "sexta", "valor": 2400},
]

# 1. Faturamento total
total = sum(f["valor"] for f in faturamento)

# 2. Dia de maior faturamento
maior = max(faturamento, key=lambda x: x["valor"])

# 3. Média de vendas
media = total / len(faturamento)

print("Exercício 1:")
print("Faturamento total:", total)
print("Dia de maior faturamento:", maior["dia"])
print("Média de vendas:", media)
print("-" * 50)


# Exercício 12 – Estoque de produtos
estoque = {
    "notebook": [5, 7, 3],
    "mouse": [20, 25, 18],
    "teclado": [12, 14, 9],
}

totais = {produto: sum(qtd) for produto, qtd in estoque.items()}
menor = min(totais, key=totais.get)

print("Exercício 2:")
print("Totais:", totais)
print("Produto com menor estoque:", menor)
print("-" * 50)


# Exercício 13 – Funcionários e salários
funcionarios = [
    {"nome": "Ana", "salario": 4500, "departamento": "RH"},
    {"nome": "Carlos", "salario": 7000, "departamento": "TI"},
    {"nome": "Beatriz", "salario": 5200, "departamento": "Financeiro"},
    {"nome": "João", "salario": 4800, "departamento": "TI"},
]

folha = sum(f["salario"] for f in funcionarios)
mais_rico = max(funcionarios, key=lambda x: x["salario"])

salarios_departamento = {}
for f in funcionarios:
    depto = f["departamento"]
    salarios_departamento.setdefault(depto, []).append(f["salario"])

print("Exercício 3:")
print("Folha total:", folha)
print("Maior salário:", mais_rico["nome"])
print("Salários por departamento:", salarios_departamento)
print("-" * 50)


# Exercício 14 – Pesquisa de satisfação
avaliacoes = {
    "loja A": [8, 9, 7, 10, 6],
    "loja B": [5, 7, 6, 8, 7],
    "loja C": [9, 8, 9, 10, 9],
}

medias = {loja: sum(notas)/len(notas) for loja, notas in avaliacoes.items()}
melhor = max(medias, key=medias.get)

print("Exercício 4:")
print("Médias:", medias)
print("Loja com maior média:", melhor)
print("-" * 50)


# Exercício 15 – Controle de vendas
vendas = [
    {"vendedor": "Marcos", "itens": {"notebook": 2, "mouse": 5}},
    {"vendedor": "Lucia", "itens": {"notebook": 1, "teclado": 3}},
    {"vendedor": "Paula", "itens": {"mouse": 4, "teclado": 2}},
]

total_notebooks = sum(v["itens"].get("notebook", 0) for v in vendas)
vendedor_top = max(vendas, key=lambda v: sum(v["itens"].values()))["vendedor"]

consolidado = {}
for v in vendas:
    for item, qtd in v["itens"].items():
        consolidado[item] = consolidado.get(item, 0) + qtd

print("Exercício 5:")
print("Notebooks vendidos:", total_notebooks)
print("Maior vendedor:", vendedor_top)
print("Consolidado:", consolidado)
print("-" * 50)


# Exercício 16 – Classificação de produtos por preço
produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 80},
    {"nome": "Teclado", "preco": 150},
    {"nome": "Cadeira", "preco": 900},
]

classificacao = {}
for p in produtos:
    if p["preco"] <= 100:
        tipo = "barato"
    elif p["preco"] <= 1000:
        tipo = "médio"
    else:
        tipo = "caro"
    classificacao[p["nome"]] = tipo

print("Exercício 6:")
print("Classificação:", classificacao)
print("-" * 50)


# Exercício 17 – Avaliação de desempenho de funcionários
funcionarios = [
    {"nome": "Ana", "nota": 9},
    {"nome": "Carlos", "nota": 6},
    {"nome": "Beatriz", "nota": 4},
    {"nome": "João", "nota": 7},
]

avaliacao = {}
for f in funcionarios:
    if f["nota"] >= 8:
        situacao = "Excelente"
    elif f["nota"] >= 5:
        situacao = "Regular"
    else:
        situacao = "Precisa melhorar"
    avaliacao[f["nome"]] = situacao

print("Exercício 7:")
print("Avaliação:", avaliacao)
print("-" * 50)


# Exercício 18 – Controle de estoque com alerta
estoque = {
    "notebook": 3,
    "mouse": 25,
    "teclado": 8,
    "monitor": 2
}

print("Exercício 8:")
for produto, qtd in estoque.items():
    if qtd < 5:
        status = "Estoque crítico"
    elif qtd < 10:
        status = "Estoque baixo"
    else:
        status = "Estoque adequado"
    print(produto, "-", status)
print("-" * 50)


# Exercício 19 – Análise de vendas por região
vendas = [
    {"regiao": "Sul", "valor": 12000},
    {"regiao": "Norte", "valor": 8000},
    {"regiao": "Sudeste", "valor": 20000},
    {"regiao": "Centro-Oeste", "valor": 5000},
]

situacao_regioes = []
for v in vendas:
    if v["valor"] >= 10000:
        situacao = "Meta atingida"
    else:
        situacao = "Meta não atingida"
    situacao_regioes.append({"regiao": v["regiao"], "situacao": situacao})

print("Exercício 9:")
print(situacao_regioes)
print("-" * 50)


# Exercício 20 – Cálculo de desconto em compras
compras = [
    {"cliente": "Maria", "valor": 450},
    {"cliente": "José", "valor": 1200},
    {"cliente": "Clara", "valor": 3000},
]

resultado = []
for c in compras:
    if c["valor"] < 500:
        desconto = 0.05
    elif c["valor"] < 2000:
        desconto = 0.10
    else:
        desconto = 0.15
    valor_final = c["valor"] * (1 - desconto)
    resultado.append({
        "Cliente": c["cliente"],
        "Valor Original": c["valor"],
        "Desconto (%)": desconto*100,
        "Valor Final": round(valor_final, 2)
    })

print("Exercício 10:")
print(resultado)
print("-" * 50)