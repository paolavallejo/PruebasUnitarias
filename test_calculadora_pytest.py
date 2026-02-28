# test_calculadora_pytest.py
import pytest
from calculadora import sumar, dividir

def test_sumar_positivos():
    assert sumar(3, 5) == 8

def test_sumar_negativos():
    assert sumar(-1, -3) == -4

def test_dividir_normal():
    assert dividir(10, 4) == 2.5

def test_dividir_por_cero_lanza_excepcion():
    with pytest.raises(ValueError):
        dividir(10, 0)




@pytest.mark.parametrize("a, b, esperado", [
    (10, 2, 5),
    (9, 3, 3),
    (7, 2, 3.5),
])
def test_dividir_varios_casos(a, b, esperado):
    assert dividir(a, b) == esperado

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)