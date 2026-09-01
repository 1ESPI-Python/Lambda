import ecommerce as ecommerce

catalogo2 = []

def menu_cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto (X.XX): "))
    estoque = int(input("Digite a quantidade em estoque: "))
    print("\n")
    
    ecommerce.cadastrar_produto(ecommerce.get_catalogo(), nome, preco, estoque)
    
menu_cadastrar_produto()
ecommerce.exibir_catalogo(ecommerce.get_catalogo())
ecommerce.atualizar_estoque("Bicicleta Vermelha", 2)
ecommerce.exibir_catalogo(ecommerce.get_catalogo())