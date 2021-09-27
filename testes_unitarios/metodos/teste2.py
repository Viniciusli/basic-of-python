import pytest
from teste import Teste


obj = Teste()


def teste1():
    assert 10 == obj.metodo_multiplicacao(2, 5)


def teste2():
    assert 4 == obj.metodo_multiplicacao(1, 2)
