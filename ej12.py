class LineaTelefonica:
    def __init__(self, numero, gigas_incluidos):
        self.numero = numero
        self.gigas_incluidos = gigas_incluidos
        self.gigas_consumidos = 0

    def registrar_consumo(self, gigas):
        if gigas <= 0:
            print("[!] El consumo debe ser mayor a cero.")
            return

        self.gigas_consumidos += gigas
        print(f"[-] Se consumieron {gigas} GB. Total acumulado: {self.gigas_consumidos} GB / {self.gigas_incluidos} GB incluidos.")
        
        if self.gigas_consumidos > self.gigas_incluidos:
            print("*** ¡AVISO! El paquete de datos contratado se ha agotado. Está consumiendo datos adicionales. ***")

    def gigas_disponibles(self):
        restantes = self.gigas_incluidos - self.gigas_consumidos
        return max(0, restantes)

    def __str__(self):
        return f"Línea: {self.numero} | Plan: {self.gigas_incluidos} GB | Disponibles: {self.gigas_disponibles()} GB"

if __name__ == "__main__":
    linea = LineaTelefonica("0982111222", 10)
    print(linea)
    linea.registrar_consumo(6)
    linea.registrar_consumo(5)
    print(linea)
