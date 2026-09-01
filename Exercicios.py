#Criar 1 função criar_aluno com parâmetros nome e idade e retorna uma lista
nome = input("Informe o nome: ")
idade = int(input("Informe a idade: "))

def criar_aluno(nome: str, idade: int) -> list[object]:
    return [nome, idade]

print(criar_aluno(nome, idade))