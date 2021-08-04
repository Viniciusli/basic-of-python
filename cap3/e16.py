# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local


total = 0


def soma(arg1, arg2):
    total = arg1 + arg2
    print("Dentro da função o total é: ", total)
    return total


# remoava os parenteses abaixo para o valor de soma global se o mesmo que o local
#total = soma(10, 20)
soma(10, 20)
print("Fora da função o total é: ", total)
