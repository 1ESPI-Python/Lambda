#Exercício 1

def mostrar_informacoes(nome = "Jorge", idade = 42, cidade = "São Palo"):
    print(f"O nome do usuário é {nome}, possui {str(idade)} anos de idade e mora em {cidade}")
    
    
#Exercício 2

def calcular_area_retangulo(base: 1, altura: 1):
    area = base * altura
    return area

#Exercício 3

def soma(a: float, b: float) -> float:
    return (a + b)

#Exercício 4

def enviar_email(destinatario, assunto = "Sem Assunto", corpo = ""):
    print(f"Destinatário: {destinatario} \nAssunto: {assunto} \nCorpo: {corpo}")
    
#Exercício 5

def concatenar_strings(string1: str, string2: str, separador: str = " ") -> str:
    return string1 + separador + string2

#Exercício 6

def comprar_produto(produto: str = "produto desconhecido", quantidade: int = 1) -> str:
    return (f"Comprou {quantidade} unidade(s) de {produto}")

#Exercício 7

def listar_itens(itens: list[str]):
    for item in itens:
        print(item)