class CuentaCorriente:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def acreditar_saldo(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"[+] Se acreditaron {monto:,.0f} Gs. Saldo actual: {self.saldo:,.0f} Gs.")
        else:
            print("[!] El monto a acreditar debe ser positivo.")

    def registrar_consumo(self, monto):
        if monto <= 0:
            print("[!] El consumo debe ser mayor a cero.")
            return
        
        if monto > self.saldo:
            print(f"[X] RECHAZADO: Consumo de {monto:,.0f} Gs. supera el saldo disponible ({self.saldo:,.0f} Gs.).")
        else:
            self.saldo -= monto
            print(f"[-] Consumo exitoso de {monto:,.0f} Gs. Saldo restante: {self.saldo:,.0f} Gs.")

    def __str__(self):
        return f"Cuenta Corriente de {self.titular} | Saldo: {self.saldo:,.0f} Gs."

if __name__ == "__main__":
    cuenta = CuentaCorriente("Ana Rojas", 50000)
    print(cuenta)
    cuenta.acreditar_saldo(100000)
    cuenta.registrar_consumo(120000)
    cuenta.registrar_consumo(40000)
    print(cuenta)
