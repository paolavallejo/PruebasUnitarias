# PruebasUnitarias

# Descripción:

Este proyecto implementa un módulo de evaluación académica que permite calcular el estado y la categoría de un estudiante a partir de su nota final y el número de faltas.

El sistema valida datos de entrada, aplica reglas de negocio y clasifica el resultado académico de forma automática, siguiendo principios de desarrollo guiado por pruebas (TDD).


# Reglas:

La nota debe estar entre 0 y 100

El estudiante aprueba si la nota es ≥ 60

El estudiante es sobresaliente si la nota es ≥ 90

Si tiene más de 3 faltas, se aplica un descuento automático de 5 puntos

No se permiten valores inválidos

No se permiten tipos de datos incorrectos


# Ejecución:

pip install pytest

pytest


# Pruebas:

1. Pruebas normales
2. Pruebas de borde
3. Pruebas de error
4. Pruebas de valores extremos
5. Pruebas de reglas de negocio
6. Pruebas de validación de datos


# Extensión:

1. Agregar categoría "EXCELENTE" entre 85–89

2. Agregar regla por inasistencia grave (>10 faltas → reprobado automático)

3. Agregar pruebas primero (TDD)

4. Introducir refactor con pruebas vivas

5. Agregar mensaje a las pruebas (assert con mensaje)

6. Agregar una prueba que verifique el tipo de una variable