import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class StudentScoreTest {

    // ==================================================
    // PRUEBAS NORMALES
    // ==================================================
    @Test
    void testAprobadoNormal() {
        String resultado = StudentScore.evaluarEstudiante(70, 1);
        assertEquals("APROBADO", resultado);
    }

    @Test
    void testReprobadoNormal() {
        String resultado = StudentScore.evaluarEstudiante(40, 0);
        assertEquals("REPROBADO", resultado);
    }

    // ==================================================
    // PRUEBAS DE BORDE
    // ==================================================
    @Test
    void testBordeAprobado() {
        String resultado = StudentScore.evaluarEstudiante(60, 0);
        assertEquals("APROBADO", resultado, "60 debe ser aprobado");
    }

    @Test
    void testBordeExcelente() {
        String resultado = StudentScore.evaluarEstudiante(85, 0);
        assertEquals("EXCELENTE", resultado, "85 debe ser excelente");
    }

    @Test
    void testBordeSobresaliente() {
        String resultado = StudentScore.evaluarEstudiante(90, 0);
        assertEquals("SOBRESALIENTE", resultado, "90 debe ser sobresaliente");
    }

    // ==================================================
    // PRUEBAS DE ERROR
    // ==================================================
    @Test
    void testNotaNegativa() {
        Exception exception = assertThrows(RuntimeException.class, () -> {
            StudentScore.evaluarEstudiante(-1, 0);
        });
        assertNotNull(exception, "Debe lanzar excepción con nota negativa");
    }

    @Test
    void testFaltasNegativas() {
        Exception exception = assertThrows(RuntimeException.class, () -> {
            StudentScore.evaluarEstudiante(80, -1);
        });
        assertNotNull(exception, "Debe lanzar excepción con faltas negativas");
    }

    // ==================================================
    // PRUEBAS DE VALORES EXTREMOS
    // ==================================================
    @Test
    void testNotaExtremaAlta() {
        Exception exception = assertThrows(RuntimeException.class, () -> {
            StudentScore.evaluarEstudiante(1000000, 0);
        });
        assertNotNull(exception);
    }

    @Test
    void testFaltasExtremasAltas() {
        Exception exception = assertThrows(RuntimeException.class, () -> {
            StudentScore.evaluarEstudiante(50, 1000000);
        });
        assertNotNull(exception);
    }

    // ==================================================
    // PRUEBAS DE REGLAS DE NEGOCIO
    // ==================================================
    @Test
    void testInasistenciaGrave() {
        String resultado = StudentScore.evaluarEstudiante(95, 11);
        assertEquals("REPROBADO", resultado, "Inasistencia grave debe reprobar");
    }

    @Test
    void testDescuentoPorFaltas() {
        // 65 - 5 = 60 → aprobado
        String resultado = StudentScore.evaluarEstudiante(65, 4);
        assertEquals("APROBADO", resultado);
    }

    // ==================================================
    // PRUEBAS DE VALIDACIÓN DE DATOS
    // ==================================================
    @Test
    void testResultadoNoNulo() {
        String resultado = StudentScore.evaluarEstudiante(80, 1);
        assertNotNull(resultado, "El resultado no debe ser null");
    }

    @Test
    void testTipoResultado() {
        String resultado = StudentScore.evaluarEstudiante(85, 0);
        assertTrue(resultado instanceof String, "El resultado debe ser String");
    }

    // ==================================================
    // ASSERTS EXPLÍCITOS (USO DIDÁCTICO)
    // ==================================================
    @Test
    void testAssertSimple() {
        String resultado = StudentScore.evaluarEstudiante(70, 0);
        assertTrue(resultado.equals("APROBADO"));
    }

    @Test
    void testAssertConMensaje() {
        String resultado = StudentScore.evaluarEstudiante(90, 0);
        assertEquals("SOBRESALIENTE", resultado, "Error en clasificación de sobresaliente");
    }

    @Test
    void testAssertBooleano() {
        String resultado = StudentScore.evaluarEstudiante(40, 0);
        assertFalse(resultado.equals("APROBADO"), "40 no puede ser aprobado");
    }

    @Test
    void testAssertMultiple() {
        String resultado = StudentScore.evaluarEstudiante(85, 0);
        assertAll(
            () -> assertNotNull(resultado),
            () -> assertTrue(resultado instanceof String),
            () -> assertEquals("EXCELENTE", resultado)
        );
    }
}