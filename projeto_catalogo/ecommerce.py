import math

NOME = 0
PRECO = 1
ESTOQUE = 2

catalogo = [
    
]

def cadastrar_produto(catalogo: list[list[object]], nome: str, preco: float, estoque: int = 0) -> list[list[object]]:
    """
    Cadastra o produto no catálogo
    
    Args:
        :catalogo: Catálogo que será atualizado
        :nome: Nome do produto que será cadastrado
        :preco: Nome do produto que será cadastrado
        :estoque: Quantidade em estoque do produto que será cadastrado
    
    Returns:
        :catalogo: Retorna o catálogo atualizado
    """
    
    produto = [nome, preco, estoque]
    catalogo.append(produto)
    return catalogo

def exibir_catalogo(catalogo: list[list[object]]) -> None:
    """
    Exibe os produtos do catálogo
    
    Args:
        :catalogo: Catálogo a ser exibido
        
    Returns:
        :None: Não há retorno
    """
    
    for produto in catalogo:        
        print(f'{produto[NOME]} - R${produto[PRECO]:.2f} (estoque: {produto[ESTOQUE]})')
        
def get_catalogo():
    return catalogo

def atualizar_estoque(nome_produto: str, quantidade: int):
    for produto in catalogo:
        if nome_produto != produto[NOME]:
            print ("Produto não encontrado")
            return
        produto[ESTOQUE] = quantidade