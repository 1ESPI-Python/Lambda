# #Exercício 1

# titulo: str = "O Pequeno Príncipe"
# paginas: int = 305
# preco: float = 29.99

# print(titulo, paginas, preco)

# #Exercício 2

# def dobrar(numero: int) -> int:
#     """ Função que retorna o dobro de um número """
#     return numero * 2

# #Exercício 3

def calcular_media(notas: list[float]) -> float:
    """
    Calcula a média de uma lista de notas
    
    Args:
        :Notas: Lista de notas
    
    Returns:
        :Média: Média das notas (sum(notas)/notas.count)
    """
    
    return sum(notas)/len(notas)

#Exercício 4

def criar_aluno(nome: str, idade: int, curso: str) -> list[object]:
    
    """
    
    Args:
        :Nome: Nome do aluno
        :Idade: Idade do aluno
        :Curso: Curso que o aluno cursa
    
    Returns:
        :Aluno: Retorna uma lista com as informações do aluno (nome, idade, curso)
    
    """
    
    
    return [nome, idade, curso]

#Exercício 5

def resumo_carrinho(precos: list[float], desconto: float) -> str:

    """
    Args:
        :Preços: Lista de preços
        :Desconto: Porcentagem de desconto
        
    Returns:
        :Preço Final: Desconto aplicado à soma dos preços (sum(precos) * (1 - (desconto/100)))
    """
    
    precoFinal = round(sum(precos)*(1 - (desconto/100)), 2)
    
    return str(f"Total: R${precoFinal}")

#Exercício 6

def somar(a: float, b: float) -> float:
    return a + b

#Exercício 7

def quadrado(numero: float) -> float:
    return numero ** 2

#Exercício 8

def soma_dos_quadrados(a: float, b: float) -> float:
    return quadrado(a) + quadrado(b)

#Exercício 9

def media(a: float, b: float, c: float) -> float:
    return (a + b + c)/3

#Exercício 10

def calcular_salario(salario: float) -> float:
    aumento: float
    
    if (salario > 2000):
        aumento = 1.07
    else:
        aumento = 1.15
    
    return salario * aumento

#Exercício 11

def soma_divisores(numeros: list[int]) -> int:
    
    i = 0
    divisor = 1
    soma = 0
    
    for numero in numeros:
        for num in range (1, numeros[i]):
            if (numeros[i] % num == 0):
                soma += num
        i += 1
    
    return soma

print (soma_divisores([6, 10]))