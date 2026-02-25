import pytest
from student_score2 import evaluar_estudiante

# =========================
# 1. Pruebas normales
# =========================
def test_aprobado_normal():
    assert evaluar_estudiante(70, 1) == "APROBADO"

def test_reprobado_normal():
    assert evaluar_estudiante(40, 0) == "REPROBADO"

# =========================
# 2. Pruebas de borde
# =========================
def test_borde_aprobado():
    assert evaluar_estudiante(60, 0) == "APROBADO"

def test_borde_sobresaliente():
    assert evaluar_estudiante(90, 0) == "SOBRESALIENTE"

# =========================
# 3. Pruebas de error
# =========================
def test_nota_negativa():
    with pytest.raises(ValueError):
        evaluar_estudiante(-10, 0)

def test_faltas_negativas():
    with pytest.raises(ValueError):
        evaluar_estudiante(80, -1)

# =========================
# 4. Valores extremos
# =========================
def test_nota_maxima():
    assert evaluar_estudiante(100, 0) == "SOBRESALIENTE"

def test_nota_minima():
    assert evaluar_estudiante(0, 0) == "REPROBADO"

# =========================
# 5. Reglas de negocio
# =========================
def test_descuento_por_faltas():
    # 65 - 5 = 60 → aprobado
    assert evaluar_estudiante(65, 4) == "APROBADO"

def test_descuento_reprobado():
    # 62 - 5 = 57 → reprobado
    assert evaluar_estudiante(62, 5) == "REPROBADO"

# =========================
# 6. Validación de datos
# =========================
def test_tipo_invalido_nota():
    with pytest.raises(TypeError):
        evaluar_estudiante("90", 1)

def test_tipo_invalido_faltas():
    with pytest.raises(TypeError):
        evaluar_estudiante(90, "dos")

# =========================
# NUEVA CATEGORÍA
# =========================
def test_categoria_excelente_minimo():
    assert evaluar_estudiante(85, 0) == "EXCELENTE"

def test_categoria_excelente_maximo():
    assert evaluar_estudiante(89, 0) == "EXCELENTE"

# =========================
# INASISTENCIA GRAVE
# =========================
def test_inasistencia_grave_reprobado():
    # aunque tenga buena nota → reprobado automático
    assert evaluar_estudiante(95, 11) == "REPROBADO"

# =========================
# REGRESIÓN (pruebas existentes siguen válidas)
# =========================
def test_sobresaliente():
    assert evaluar_estudiante(90, 0) == "SOBRESALIENTE"

def test_aprobado():
    assert evaluar_estudiante(70, 1) == "APROBADO"