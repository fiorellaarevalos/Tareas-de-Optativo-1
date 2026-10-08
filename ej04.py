class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Libro: '{self.titulo}' - Autor: {self.autor} | Estado: {estado}"

if __name__ == "__main__":
    l1 = Libro("Cien años de soledad", "Gabriel García Márquez", True)
    l2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", False)
    
    print(l1)
    print(l2)
