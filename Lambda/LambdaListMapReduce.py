#Lambda
#Funcao anonima (pequena - inline)
#A criação da função está próxima do uso dela
#Versáteis
#Cuidado que temos que ter é NÃO TENTAR RESOLVER TUDO COM LAMBDA
#Se vc fizer isso, seu programa fica ilegível

#Numa função tradicional fariamos:
def dobro (n: float) -> float:
    return n * 2

#Transformar em lambda
#Sintaxe lambda <argumentos> : <retorno>
#Lambda SEMPRE TEM O RETURN
ldobro = lambda n: n * 2

#O uso mais comum
print((lambda n: n* 2) (50))

#Lambda CONDICIONAL
#Tem um if embutido

#Funcao que decide qual o maior de 2 numeros
def maior (x: int, y: int) -> int:
    if x > y:
        return x
    else:
        return y
    
#Transformar em lambda
print((lambda x, y: x if x > y else y) (25, 50))

#Posso usar o print dentro do lambda?
#Pode, mas cuidado
# lmenor = lambda x, y: print(x) if x < y else print(y)
# xpto = lmenor (9, 65)
# print (lmenor(9, 60))

#A melhor solução
lmenor2 = lambda x, y: \
    f"Entre {x} e {y}, o menor número é {x}" \
        if x < y else \
            f"Entre {x} e {y}, o menor número é {y}"
print(lmenor2 (50, 100))