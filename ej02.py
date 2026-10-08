class Producto:
    def __init__(self, nombre, precio_unitario, stock):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.stock = stock

    def calcular_valor_stock(self):
        return self.precio_unitario * self.stock

    def __str__(self):
        return f"Producto: {self.nombre} | Precio Unitario: {self.precio_unitario:,.0f} Gs. | Stock: {self.stock} unidades | Valor Total Stock: {self.calcular_valor_stock():,.0f} Gs."

if __name__ == "__main__":
    p1 = Producto("Yerba Mate 1kg", 25000, 15)
    p2 = Producto("Fideo 500g", 7500, 30)
    
    print(p1)
    print(p2)
