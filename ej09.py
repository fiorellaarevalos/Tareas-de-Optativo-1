class Turno:
    def __init__(self, paciente, hora):
        self.paciente = paciente
        self.hora = hora
        self.estado = "Pendiente"

    def marcar_atendido(self):
        self.estado = "Atendido"

    def __str__(self):
        return f"[{self.hora}] Paciente: {self.paciente} - Estado: {self.estado}"

class Agenda:
    def __init__(self):
        self.turnos = []

    def agregar_turno(self, turno):
        self.turnos.append(turno)

    def listar_pendientes(self):
        print("\n--- TURNOS PENDIENTES ---")
        pendientes = [t for t in self.turnos if t.estado == "Pendiente"]
        if not pendientes:
            print("No hay turnos pendientes.")
        for t in pendientes:
            print(t)
        print("-------------------------")

if __name__ == "__main__":
    agenda = Agenda()
    t1 = Turno("Carlos Ruiz", "08:00")
    t2 = Turno("Elena Gómez", "08:30")
    t3 = Turno("Mario Duarte", "09:00")

    agenda.agregar_turno(t1)
    agenda.agregar_turno(t2)
    agenda.agregar_turno(t3)

    agenda.listar_pendientes()

    t1.marcar_atendido()
    print("\n(Se atendió a Carlos Ruiz)")

    agenda.listar_pendientes()
