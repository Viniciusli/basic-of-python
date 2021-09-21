from typing import Protocol


# crie um classe Televisão e uma classe ControleRemoto
# o controle aumenta o volume da tv e muda de canal

class Televisao:

    on_off = False
    volume = 0
    canal = 0
    aplicativos = ['netflix', 'prime vídeo', 'hbo max', 'youtube', 'internet']

    def __init__(self) -> None:
        self.__marca = "samsumg"
        self.__polegadas = 75
        self.onde_estou = Televisao.canal

    def __str__(self) -> str:
        return f"Você está assistindo: {self.onde_estou}\nVolume: {self.volume}\n"


class Controle(Televisao):

    def __init__(self) -> None:
        super().__init__()

    def on(self):
        self.on_off = True

    def off(self):
        self.on_off = False

    def aumenta_volume(self):
        if self.volume == 100:
            print("Volume máximo")
        else:
            self.volume += 1

    def reduz_volume(self):
        if self.volume == 0:
            print("Volume mínimo")
        else:
            self.volume -= 1

    def aumenta_canal(self, user_canal: int = 1):
        self.onde_estou += user_canal

    def reduz_canal(self, user_canal: int = 1):
        self.canal -= user_canal

    def entra_app(self, user_app: list = Televisao.aplicativos):
        for app in user_app:
            print(f"* {app}")
        escolha = input("selecione um app: ")
        if escolha in user_app:
            self.onde_estou = escolha

    def __str__(self) -> str:
        return super().__str__()


controle = Controle()
controle.aumenta_canal()
