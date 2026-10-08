class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def descripcion_comercial(self):
        return f"{self.marca} {self.modelo} {self.anio} - {self.precio:,.0f} Gs."

    def __str__(self):
        return self.descripcion_comercial()

if __name__ == "__main__":
    v1 = Vehiculo("Toyota", "Corolla", 2020, 95000000)
    v2 = Vehiculo("Kia", "Rio", 2022, 72000000)
    
    print(v1)
    print(v2)
