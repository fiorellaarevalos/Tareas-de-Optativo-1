class ProductoAlmacenControlado:
    def __init__(self, nombre, precio, stock_inicial, stock_minimo):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock_inicial
        self.stock_minimo = stock_minimo

    def ingresar_mercaderia(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad
            print(f"[+] Ingreso de {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}")
        else:
            print("[!] La cantidad a ingresar debe ser mayor a cero.")

    def registrar_venta(self, cantidad):
        if cantidad <= 0:
            print("[!] La cantidad a vender debe ser mayor a cero.")
            return

        if cantidad > self.stock:
            print(f"[X] Venta cancelada: No hay suficiente stock de {self.nombre} (Stock disponible: {self.stock}).")
        else:
            self.stock -= cantidad
            print(f"[-] Venta de {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}")
            self.verificar_stock_minimo()

    def verificar_stock_minimo(self):
        if self.stock < self.stock_minimo:
            print(f"*** ¡ALERTA DE REPOSICIÓN! El producto '{self.nombre}' está por debajo del mínimo ({self.stock} < {self.stock_minimo}). ***")

    def __str__(self):
        return f"Producto: {self.nombre} | Stock: {self.stock} (Mínimo: {self.stock_minimo})"

if __name__ == "__main__":
    prod = ProductoAlmacenControlado("Arroz 1kg", 8000, 10, 5)
    print(prod)
    prod.registrar_venta(7)
    prod.ingresar_mercaderia(10)
