public class StudentScore {

    public static String evaluarEstudiante(int nota, int faltas) {

        // Regla crítica
        if (faltas > 10) {
            return "REPROBADO";
        }

        // Regla de negocio
        if (faltas > 3) {
            nota = nota - 5;
        }

        // Clasificación
        if (nota < 60) {
            return "REPROBADO";
        } 
        else if (nota < 85) {
            return "APROBADO";
        } 
        else if (nota < 90) {
            return "EXCELENTE";
        } 
        else {
            return "SOBRESALIENTE";
        }
    }
}