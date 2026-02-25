def es_palindromo(texto: str) -> bool:
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]