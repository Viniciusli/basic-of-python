# Exercício 10 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"


import pandas as pd


df_arquive = pd.read_csv("cap3/binary.csv")
print(df_arquive.describe())
