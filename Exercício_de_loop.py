#1
lista_1 = ["maçã", "banana", "laranja", "uva"]
print(lista_1)
#2
lista_1[0]
lista_1[-1]
#3
lista_1.insert(4, "manga")
print(lista_1)
#4
lista_1.remove("banana")
print(lista_1)
#5
lista_1[1]="abacaxi"
print(lista_1)
#6
lista_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#7
soma = sum(lista_2)
print(soma)
#8
maior_número = max(lista_2)
menor_número = min(lista_2)
print("O maior número da lista é:", maior_número)
print("O menor número é:", menor_número)
#9
lista_2.reverse()
print(lista_2)
#10
lista_3 = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
print(lista_3)
#11
lista_3.sort()
print(lista_3)
#12
lista_3.insert(4, "Porto Alegre")
print(lista_3)
#13
indice=lista_3.index("Curitiba")
print("O índice de Curitiba na lista é:", indice)
#14
lista_3.remove("Rio de Janeiro")
print(lista_3)
#15
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
print(lista_a)
print(lista_b)
#16
lista_c = lista_a + lista_b
#17
print(lista_c)
#18
animais_domésticos=["cachorro", "gato", "coelho"]
animais_selvagens=["leão", "tigre", "urso"]
print(animais_domésticos)
print(animais_selvagens)
#19
todos_animais = animais_selvagens + animais_domésticos
#20
print(todos_animais)

#looping com for

#21
nomes = ["Ana", "Pedro", "Maria", "João"]
#22
for nome in nomes: print(nome)
#23
nomes_maiusculos=[nome.upper() for nome in nomes]
print(nomes_maiusculos)
#24
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for num in numeros:
    if num %2 == 0:
        print(num)
#25
quadrados = [num ** 2 for num in numeros]
print(quadrados)
#26
palavras = [ "python", "java", "c", "javascript"]
for palavra in palavras:
    print(f"{palavra} tem {len(palavra)} letras.")
#27
idade = [12, 18, 25, 40, 60]
print(idade)
for idades in idade:
    if idades >= 18:
        print (f"{idades} = maior de idade")
    else: 
        idades < 18
        print(f"{idades} = menor de idade")
#28
notas = [5.5, 7.0, 8.3, 4.9, 6.2]
for nota in notas:
    if nota >=7:
        print(f"{nota} Aprovado")
    else:
        nota < 7
        print(f"{nota} Reprovado")
#29
lista = ["arara", "banana", "radar", "python"]
for words in lista:
    if words == words[:: -1]:
        print(words, "é um palindromo")
    else:
        print(words, "Náo é um palindromo")
#30
compras = ["arroz", "feijão", "batata", "carne"]
for alimento in compras:
    print("preciso comprar,", alimento)
#31
numero = 1
while numero <= 10:
    print(numero)
    numero +=1
#32
N = int(input("digite um número inteiro"))
while N != 0:
    print(N)
    N = int(input("digite um número inteiro"))
print("programa encerrado")
#33
num = 1
soma = 0
while num <= 100:
    soma += num
    num += 1
print("A soma de 1 a 100 é:", soma)
#34
segredo = int(input("digite um número secreto"))
while segredo != 7:
    print("errou tente novamente")
    segredo = int(input("digite um número secreto"))
    print("número primo e considerado o número da sorte")
    segredo = int(input("digite um número secreto"))
print("Correto")
#35
num = 2
pares = 0
while num <= 20:
    print(num)
    num += 2
    
print ("hello word")












