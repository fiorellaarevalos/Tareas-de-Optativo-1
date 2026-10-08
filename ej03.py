class Empleado:
    def __init__(self, nombre, cargo, salario_mensual):
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def calcular_salario_anual(self):
        return self.salario_mensual * 13

    def __str__(self):
        return f"Empleado: {self.nombre} | Cargo: {self.cargo} | Salario Mensual: {self.salario_mensual:,.0f} Gs. | Salario Anual (Inc. Aguinaldo): {self.calcular_salario_anual():,.0f} Gs."

if __name__ == "__main__":
    e1 = Empleado("Juan Pérez", "Analista de Sistemas", 6500000)
    print(e1)
