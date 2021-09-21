# Exercício 10 - Considere a lista abaixo e retorne apenas os elementos cujo índice for
# maior que 5.


lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for itens in enumerate(lista):
    if itens[0] > 5:
        print(itens[1])
