# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de
# elementos. Faça duas chamadas à função, com apenas 1 elemento e na segunda chamada
# com 4 elementos


def mostra_itens(item1, *args):
    print(item1)
    if len(args) != 0:
        print(args[0])


mostra_itens(10, [12, 13, 14])
