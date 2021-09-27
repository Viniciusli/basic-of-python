import pytest
import teste


# primeiro teste
def teste1():
    assert 5 == teste.soma(3, 2)


# teste com erro
def teste2():
    assert 6 == teste.soma(2, 2)
