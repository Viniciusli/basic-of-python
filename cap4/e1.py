# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada
# elemento.


from random import randint


numeros = [randint(0, 100) for x in range(3)]
print(numeros)
print(list(map(lambda y: y**3, numeros)))
