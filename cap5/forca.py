from random import choice


tabela = [
    """
    _____
    |   |
        |
        |
        |
        |
    =========""", """
    _____
    |   |
    O   |
        |
        |
        |
    =========""",
    """
    _____
    |   |
    O   |
    |   |
        |
        |
    =========""",
    """
    _____
    |   |
    O   |
   /|   |
        |
        |
    =========""",
    """    
    _____
    |   |
    O   |
   /|\  |
        |
        |
    =========""",
    """
    _____
    |   |
    O   |
   /|\  |
   /    |
        |
    =========""",
    """
    _____
    |   |
    O   |
   /|\  |
   / \  |
        |
    ========="""
]


class Forca:

    game_over = False
    win = False
    letras_corretas = set()
    letras_erradas = set()
    MAX_LETRAS_ERRADAS = 6

    def __init__(self, palavra: str) -> None:
        self.palavra = palavra

    def adivinha(self, letra: str) -> bool:
        if letra in self.palavra:
            self.letras_corretas.add(letra)
            self.vitoria()
            return True
        self.letras_erradas.add(letra)
        self.termino()
        return False

    def termino(self):
        if (len(self.letras_erradas) == self. MAX_LETRAS_ERRADAS) or self.vitoria():
            self.game_over = True
        return self.game_over

    # compara 2 vetores, letras_da_palavra_correta (da palavra da forca)
    # e letras_corretas (do usuario). Se forem iguais, vitória
    def vitoria(self) -> bool:
        letras_da_palavra_correta = set(self.palavra)
        if self.letras_corretas == letras_da_palavra_correta:
            self.game_over = True
            return True
        else:
            return False

    def palavra_escondida(self) -> list:
        letras_escondidas = []
        for letra in self.palavra:
            if letra in self.letras_corretas:
                letras_escondidas.append(letra)
            else:
                letras_escondidas.append('_')
        return letras_escondidas

    def status(self) -> str:
        return f"""
        {tabela[len(self.letras_erradas)]}
        Palavra: {" ".join(self.palavra_escondida())}
        Letras erradas: {" ".join(self.letras_erradas)}
        Letras corretas: {" ".join(self.letras_corretas)}\n"""


def escolhe_palavra():
    with open("cap5/forca_palavras.txt", "r") as arquivo:
        palavras = arquivo.read().split('\n')
    return choice(palavras)


def main():
    forca = Forca(escolhe_palavra())

    while not forca.game_over:
        print(forca.status())

        user_letra = input("Digite uma letra: ")
        forca.adivinha(user_letra)

    if forca.vitoria() == True:
        print(forca.status())
        print('\nParabéns! Você venceu!!')
    else:
        print(forca.status())
        print("\nGame over! Você perdeu.")
        print("A palavra era " + forca.palavra)


if __name__ == "__main__":
    main()
