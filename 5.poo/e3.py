# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a
# classe MP3Player com os atributos capacidade. A classe MP3player deve herdar os
# atributos da classe Smartphone.


class Smartphone:
    def __init__(self, tamanho, interface) -> None:
        self.tamanho = tamanho
        self.interface = interface


class Mp3player(Smartphone):
    def __init__(self, tamanho, interface, capacidade) -> None:
        super().__init__(tamanho, interface)
        self.capacidade = capacidade

    def __str__(self) -> str:
        return "Tamanho: %d\nInterface: %s\nCapacidade: %d" % (self.tamanho, self.interface, self.capacidade)


mp3 = Mp3player(capacidade=500, tamanho=27, interface="samsumg")
print(str(mp3))
