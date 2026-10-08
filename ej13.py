class Habitacion:
    def __init__(self, numero, tipo, tarifa_noche):
        self.numero = numero
        self.tipo = tipo
        self.tarifa_noche = tarifa_noche
        self.ocupada = False

    def ocupar(self):
        if self.ocupada:
            print(f"[X] La habitación {self.numero} ya se encuentra ocupada.")
        else:
            self.ocupada = True
            print(f"[+] Habitación {self.numero} ocupada con éxito.")

    def liberar(self):
        if not self.ocupada:
            print(f"[!] La habitación {self.numero} ya está libre.")
        else:
            self.ocupada = False
            print(f"[-] Habitación {self.numero} liberada correctamente.")

    def calcular_costo_estadia(self, noches):
        return self.tarifa_noche * noches

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Libre"
        return f"Habitación N° {self.numero} ({self.tipo}) - Tarifa: {self.tarifa_noche:,.0f} Gs./noche | Estado: {estado}"

if __name__ == "__main__":
    hab = Habitacion(204, "Doble", 250000)
    print(hab)
    hab.ocupar()
    print(hab)
    noches = 3
    costo = hab.calcular_costo_estadia(noches)
    print(f"Costo total por {noches} noches: {costo:,.0f} Gs.")
    hab.liberar()
    print(hab)
