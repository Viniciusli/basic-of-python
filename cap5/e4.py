# crie uma classe para representar uma pessoa, com atributos privados de nome, idade e
# altura. Crie os métodos necessários para sets e gets e também um método para imprimir
# os dados de uma pessoa.


class Pessoa:

    def __init__(self, nome, idade, altura) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    @property
    def dados(self):
        return f"nome: {self.__nome}\nidade: {self.__idade}\naltura: {self.__altura}"

    @dados.setter
    def nome(self, valor):
        self.__nome = valor

    @dados.setter
    def idade(self, valor):
        self.__idade = valor

    @dados.setter
    def altura(self, valor):
        self.__altura = valor
