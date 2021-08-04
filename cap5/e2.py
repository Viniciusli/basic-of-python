# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone
# e e-mail. Use pelo menos 2 métodos especiais na sua classe. Crie um objeto da sua
# classe e faça uma chamada a pelo menos um dos seus métodos especiais.

from typing import get_type_hints


class Pessoa:

    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email

    def __str__(self) -> str:
        return "Nome: %s\nCidade: %s\nTelefone: %d\nE-mail: %s" % (self.nome, self.cidade, self.telefone, self.email)

    def __len__(self):
        cont = 0
        for letter in self.nome:
            cont += 1
        return cont


cad1 = Pessoa("vinicius", "belem", 91985265049, "viniciusleeg@outlook.com")
print(str(cad1))
print("Caracteres no nome: ", len(cad1))
