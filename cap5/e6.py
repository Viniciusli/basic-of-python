# crie uma clsse Elevador.
# attrs: andar atual, total de andares (exluindo terreo), capacidade do elevador,
# e quantidade de pessoas presentes nele
# métodos: incializa, recebe a capacidade, total de andares, entra, acrescenta uma pessoa
# sai, subtrae uma pessoa, sobe, sobe um andar, desce, desce um andar
# nesse exercício eu vou adotar o prédio como tendo 10 andares =)

class Elevador:
    __capacidade = 10

    def __init__(self) -> None:
        self._terreo = 0
        self.andar_atual = self._terreo
        self.qtd_pessoas = 0
        self.andares = 10

    def entra(self) -> int:
        if self.qtd_pessoas < Elevador.__capacidade:
            self.qtd_pessoas += 1
        elif self.qtd_pessoas >= Elevador.__capacidade:
            print("Capacidade máxima atingida\nPegue outro elevador")

    def sai(self) -> int:
        if self.qtd_pessoas == 0:
            print("Não tem ninguém")
        else:
            self.qtd_pessoas -= 1

    def sobe(self, andar):
        if andar > 10:
            print("O prédio só vai até o 10º andar")
        else:
            self.andar_atual += andar - self.andar_atual

    def desce(self, andar):
        if andar < 0:
            print("O térreo é o 0.\nNão tem mais prédio para baixo disso")
        else:
            self.andar_atual -= self.andar_atual - andar

    def __str__(self) -> str:
        return f"Andar atual: {self.andar_atual}\nNúmero de pessoas: {self.qtd_pessoas}\nCapacidade: {Elevador.__capacidade}"
