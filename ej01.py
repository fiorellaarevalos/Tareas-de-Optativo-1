class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre} | Cédula: {self.cedula} | Teléfono: {self.telefono}"

if __name__ == "__main__":
    c1 = Cliente("María Gómez", "4.567.890", "0981123456")
    c2 = Cliente("Carlos Benítez", "3.210.987", "0972654321")
    
    print(c1)
    print(c2)
