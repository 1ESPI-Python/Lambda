# Python tem tipagem dinâmica

x = 10
nome = "Jorge"


print(type(nome))

#Type Hints ajuda a definir o tipo de dado esperado na variável
#mas é apenas uma AJUDA, ou seja o python não impede que seja atribuído
#um valor com outro tipo de dado.

nome: str = "Jorge"

print(type(nome))

nome = 10
print(type(nome))

preco: float
preco = 7.8

#todos os tipos de dados são aceitos no type hints
disponivel: bool = True
print(type(disponivel))

#o tipo de uso mais importante é quando definimos funcoes

def calcular_total(preco: float, quantidade: int) -> float:
    return preco * quantidade

print(calcular_total(preco, 2))
print(calcular_total(preco, 3))

#e quando a funcao nao tem retorno?

def exibir_produto(produto: str, preco: float) -> None:
    print(f"{produto} - {preco}")
    
exibir_produto('Leite', 9.8)

minhaLista:list = {'cafe', 'chantilly', 'biscoito'}
print(minhaLista)

dadosPessoais = ['Patrícia', 56, 'Feminino', 'Superior']
print(dadosPessoais)
print(f'Nome: {dadosPessoais[0]}')
print(f'Idade: {dadosPessoais[1]}')
dadosPessoais.append('Professora')
print(dadosPessoais)
print("Imprimindo a lista elemento a elemento:")

for item in dadosPessoais:
    print(item)

def somar_precos(precos: list) -> float:
    total: float = 0
    for preco in precos:
        total += preco
    return total

print('\nSomando preços')
print(f'total: {somar_precos([10,20,30])}')
#print(preco)

def criar_produto(produto: str, preco: float, quantidade: int) -> list:
    return [produto, preco, quantidade]

print(f'\nCriar Estoque')
print(f'Estoque: {criar_produto('Leite', 8.9, 10)}')

#tipo de dados generico: object
#quando usar -> na assinatura da função

idades: list[int] = [17, 56, 23]
print(f"Idades: {idades}")

#mas se eu quisesse uma lista mista
produto = {"camisa", 29.9, 8}
print(f"Produto: {produto}")
produto: list[object] = {"camisa", 29.9, 8}

#DOCSTRING
def calcular_total(preco: float, quantidade: int) -> float:
    """  Calcula a quantidade total de um produto
    
    Args:
        :Preço: Preço unitario do produto
        :Quantidade: Quantidade total de um produto
    
    Returns:
        :Total: Preco total (preco * quantidade)
    """
    
    return preco * quantidade