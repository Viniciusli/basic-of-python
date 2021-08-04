# crie uma classe Agenda para armazenar dados de pessoas, nome, idade, altura
# métodos: cadastrar uma pessoa nova, remover uma pessoa, buscar uma pessoa,
# imprimir a agenda e imprimir uma pessoa


class Agenda:

    def __init__(self) -> None:
        self.pessoas = []

    def armazena_pessoa(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        dados_pessoa = {
            'nome': self.nome,
            'idade': self.idade,
            'altura': self.altura
        }
        self.pessoas.append(dados_pessoa)

    def remove(self, nome):
        for pessoa in self.pessoas:
            if pessoa['nome'] == nome:
                [pessoa.pop(chave) for chave in ['nome', 'idade', 'altura']]

        self.pessoas.pop(self.pessoas.index({}))

    def busca_pessoa(self, nome):
        for pessoa in self.pessoas:
            if pessoa['nome'] == nome:
                print(f"{nome} está na {self.pessoas.index(pessoa)} posição")

    def imprime_agenda(self):
        for pessoa in self.pessoas:
            for chave, valor in pessoa.items():
                print(f"{chave}: {valor}")
            print("\n")

    def imprime_pessoa(self, indice):
        for pessoa in self.pessoas:
            if self.pessoas.index(pessoa) == indice:
                for chave, valor in pessoa.items():
                    print(f"{chave}: {valor}")
