class ProductoItem:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class ItemCarrito:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad} un. | Subtotal: {self.calcular_subtotal():,.0f} Gs."

class Carrito:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def calcular_total(self):
        return sum(item.calcular_subtotal() for item in self.items)

    def __str__(self):
        resultado = "=== DETALLE DEL CARRITO ===\n"
        for item in self.items:
            resultado += f" - {item}\n"
        resultado += f"TOTAL GENERAL: {self.calcular_total():,.0f} Gs."
        return resultado

if __name__ == "__main__":
    p1 = ProductoItem("Teclado Mecánico", 150000)
    p2 = ProductoItem("Mouse Gamer", 80000)

    item1 = ItemCarrito(p1, 1)
    item2 = ItemCarrito(p2, 2)

    carrito = Carrito()
    carrito.agregar_item(item1)
    carrito.agregar_item(item2)

    print(carrito)
