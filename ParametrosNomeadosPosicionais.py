#Funções: outros temas

#Parametros nomeados = posicionais

def calcular_media(python: float, webdev: float, frontend: float) ->float:
    """
    Calcula média
    """
    
    return (python + webdev + frontend) / 3

media = calcular_media(9, 8, 9.5)
#racional
#1 posicao se refere a nota de python
#2 posicao se refere a nota de webdev
#3 posicao se refere a nota de frontend

print(f"Média: {media:.1f}")

#parametros nomeados
media = calcular_media(webdev=9, frontend= 7, python= 9.5)
print(f"Média: {media:.1f}")

#cuidado com a mistura
#não funciona parametro nomeado na frente de posicional
# media = calcular_media(python = 9.5, 8, 7)

#a /= 100
#a = a / 100