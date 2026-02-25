import pytest
from palindromo import es_palindromo

# =========================
# Palabras palíndromas simples
# =========================

def test_palabra_simple():
    assert es_palindromo("radar") is True

# =========================
# Frases palíndromas
# =========================

def test_frase_con_espacios():
    assert es_palindromo("anita lava la tina") is True

# =========================
# No palíndromos
# =========================

def test_no_palindromo():
    assert es_palindromo("python") is False

# =========================
# Cadenas vacías
# =========================

def test_cadena_vacia():
    assert es_palindromo("") is True  # diseño esperado

# =========================
# Sensibilidad a mayúsculas/minúsculas
# =========================

def test_mayusculas():
    assert es_palindromo("Radar") is True