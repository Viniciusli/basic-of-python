# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da
# variável for menor ou igual a 20, adicione à lista, apenas os valores pares
# e imprima a lista

lista = []
numero = 4

while (numero <= 20):
    if numero % 2 == 0:
        lista.append(numero)
    numero += 1
print(lista)
