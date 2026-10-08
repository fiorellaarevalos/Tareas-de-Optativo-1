class Cancion:
    def __init__(self, titulo, artista, duracion_minutos):
        self.titulo = titulo
        self.artista = artista
        self.duracion_minutos = duracion_minutos

    def __str__(self):
        return f"'{self.titulo}' - {self.artista} ({self.duracion_minutos} min)"

class ListaReproduccion:
    def __init__(self, nombre_lista):
        self.nombre_lista = nombre_lista
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def calcular_duracion_total(self):
        total = sum(c.duracion_minutos for c in self.canciones)
        return total

    def __str__(self):
        detalle = f"Lista: {self.nombre_lista}\nCanciones:\n"
        for c in self.canciones:
            detalle += f" - {c}\n"
        detalle += f"Duración total: {self.calcular_duracion_total()} minutos"
        return detalle

if __name__ == "__main__":
    c1 = Cancion("Bohemian Rhapsody", "Queen", 6)
    c2 = Cancion("Hotel California", "Eagles", 7)
    c3 = Cancion("Stairway to Heaven", "Led Zeppelin", 8)

    mi_lista = ListaReproduccion("Clásicos del Rock")
    mi_lista.agregar_cancion(c1)
    mi_lista.agregar_cancion(c2)
    mi_lista.agregar_cancion(c3)

    print(mi_lista)
