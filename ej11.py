class Estudiante:
    def __init__(self, nombre, nota_minima_aprobacion=60):
        self.nombre = nombre
        self.materias = {} 
        self.nota_minima = nota_minima_aprobacion

    def registrar_nota(self, materia, nota):
        self.materias[materia] = nota

    def calcular_promedio(self):
        if not self.materias:
            return 0
        return sum(self.materias.values()) / len(self.materias)

    def esta_aprobado(self):
        return self.calcular_promedio() >= self.nota_minima

    def __str__(self):
        boletin = f"Boletín de Calificaciones: {self.nombre}\n"
        for mat, nota in self.materias.items():
            boletin += f" - {mat}: {nota}\n"
        promedio = self.calcular_promedio()
        condicion = "APROBADO" if self.esta_aprobado() else "REPROBADO"
        boletin += f"Promedio Final: {promedio:.2f} | Condición: {condicion}"
        return boletin

if __name__ == "__main__":
    est = Estudiante("Sofía Giménez", 60)
    est.registrar_nota("Programación I", 85)
    est.registrar_nota("Base de Datos", 75)
    est.registrar_nota("Matemática", 90)

    print(est)
