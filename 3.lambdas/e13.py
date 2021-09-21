# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos,
# adicione 2 elementos a lista e imprima a lista

def add_elements(lista):
    lista.append("cupuaçu")
    lista.append("manga")
    return lista


frutas = ["abacaxi", "uva", "maçã", "maracuja"]
print("lista de frutas: ", frutas)

add_elements(frutas)

print("lsita de frutas atualizada: ", frutas)
