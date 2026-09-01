from functools import reduce

#Exercício 1
dobro = lambda x: x * 2

#Exercício 2
par_ou_impar = lambda x: "par" if x % 2 == 0 else "ímpar"

#Exercício 3
precos = [100.0, 250.0, 39.90]

precosDesconto = list(map((lambda preco: preco * 0.9), precos))
print(precosDesconto)

#Desafio
descontos = [0.1, 20, 0.05]

precosDesconto2 = list(map((lambda preco, desconto: round(preco * (1 - desconto), 2) if desconto < 1 else round(preco * (1 - (desconto/100)))), precos, descontos))
print (precosDesconto2)

#Exercício 4
def para_maiuscula(texto: str) -> str:
    return texto.upper()

nomes = ["ana", "bruno", "carla"]
nomesUpper = list(map(para_maiuscula, nomes))
print(nomesUpper)

#Exercício 5

numeros = [2, 3, 4, 5]

def multiplicar(num1: int, num2: int) -> int:
    return num1 * num2

numMult = reduce(multiplicar, numeros)
print (numMult)

#Exercício 6
numeros = [15, 42, 8, 99, 23]

maiorNum = reduce(lambda x, y: x if x < y else y, numeros)
print (maiorNum)

#Exercício 7
quadrados = [item ** 2 for item in range(1, 11)]
print (quadrados)

#Exercício 8
numeros = [3, 8, 15, 22, 7, 40, 11]

pares = [item for item in numeros if item % 2 == 0]
print (pares)

#Exercício 9
numeros = [3, 8, 15, 22, 7]

par_ou_impar2 = ["par" if numero % 2 == 0 else "ímpar" for numero in numeros]
print (par_ou_impar2)

#Exercício 10
NOME, PRECO, ESTOQUE = 0, 1, 2
produtos = [
    ["Caderno", 12.50, 5],
    ["Caneta", 2.30, 100],
    ["Mochila", 89.90, 3],
    ["Estojo", 15.00, 8],
]

produtosAcabando = [produto[NOME] for produto in produtos if produto[ESTOQUE] < 10]
print (produtosAcabando)