def validar_datos(nota, faltas):
    if not isinstance(nota, int):
        raise TypeError("La nota debe ser entera")
    if not isinstance(faltas, int):
        raise TypeError("Las faltas deben ser enteras")
    if nota < 0 or nota > 100:
        raise ValueError("Nota fuera de rango")
    if faltas < 0:
        raise ValueError("Faltas inválidas")


def aplicar_reglas(nota, faltas):
    if faltas > 10:
        return "REPROBADO"

    if faltas > 3:
        nota -= 5

    return clasificar(nota)


def clasificar(nota):
    if nota < 60:
        return "REPROBADO"
    if nota < 85:
        return "APROBADO"
    if nota < 90:
        return "EXCELENTE"
    return "SOBRESALIENTE"


def evaluar_estudiante(nota, faltas):
    validar_datos(nota, faltas)
    return aplicar_reglas(nota, faltas)