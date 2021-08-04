def operacao(op, numeros):
    if op == 1:
        return sum(numeros)
    elif op == 2:
        sub = 0
        for num in numeros:
            sub -= num
        return sub
    elif op == 3:
        multi = 1
        for num in numeros:
            multi *= num
        return multi
    elif op == 4:
        return numeros[0] / numeros[1]
    else:
        return "Operação Inválida!\nInforme um número válido"


print("\n******************* Python Calculator *******************")

numeros = []
user = int(input("""OPERAÇÕES:

1: soma
2: subtração
3: multiplicação
4: divisão

Selecione a operação desejada: """))

user_numeros = ""
while (True):
    ordem = 1
    user_numeros = input(
        "Digite o %dº número da operação ('sair' para calcular): " % ordem)
    ordem += 1
    if user_numeros != "sair":
        numeros.append(int(user_numeros))
    else:
        break

resultado = operacao(user, numeros)
print(f"Resultado: {resultado}")
