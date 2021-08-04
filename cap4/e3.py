# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.


# forma 1
matriz = [[1, 2], [3, 4], [5, 6], [7, 8]]
for linha in matriz:
    print(linha)
print("-="*20)
matriz_transposta = list(zip(matriz[0], matriz[1], matriz[2], matriz[3]))
for linha in matriz_transposta:
    print(linha)

print("-="*20)
# forma 2
matriz = [[1, 2], [3, 4], [5, 6], [7, 8]]
for linha in matriz:
    print(linha)
print("-="*20)

transposta = [[linha[i] for linha in matriz] for i in range(2)]
for linha in transposta:
    print(linha)
