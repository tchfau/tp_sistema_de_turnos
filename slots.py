from datetime import datetime

class Slot:
    def __init__(self, **kwargs):
        # Asigna directamente los valores del CSV
        for clave, valor in kwargs.items():
            setattr(self, clave.strip().lower(), str(valor).strip())

        # Estado en memoria (por defecto todos disponibles)
        self.estado = "disponible"

        # Normaliza el horario al formato HH:MM
        hora = datetime.strptime(self.hora.strip(), "%H:%M")
        self.hora = hora.strftime("%H:%M")

    def __str__(self):
        return f"{self.dia} - {self.hora} ({self.estado})"


class GestorSlots:
    def __init__(self, db_slots):
        self.db_slots = db_slots
        self.transf_slots, self.slots = self.db_slots.read()

        # Inicializa todos los slots como disponibles
        i = 0
        while i < len(self.slots):
            slot = self.slots[i]
            if not hasattr(slot, "estado"):
                slot.estado = "disponible"
            i = i + 1

    def validar_dia(self, dia_str):
        # Valida que el día sea un número entero entre 1 y 31
        try:
            dia = int(dia_str.strip())
            return dia >= 1 and dia <= 31
        except:
            return False

    def validar_hora(self, hora_str):
        # Valida el formato HH:MM usando datetime
        try:
            datetime.strptime(hora_str.strip(), "%H:%M")
            return True
        except:
            return False

    def listar_slots(self, dia_filtrado=None):
        if not self.slots:
            print("No hay horarios disponibles.")
            return

        print("HORARIOS DISPONIBLES:")
        i = 0
        hay_disponibles = False
        while i < len(self.slots):
            slot = self.slots[i]
            if (dia_filtrado is None or str(slot.dia) == str(dia_filtrado)) and slot.estado == "disponible":
                print(f"[{i + 1}] Día {slot.dia} - {slot.hora}")
                hay_disponibles = True
            i = i + 1

        if not hay_disponibles:
            print("No hay horarios disponibles para ese día.")

    def seleccionar_slot(self):
        if not self.slots:
            print("No hay slots cargados.")
            return None

        dia_ingresado = input("Ingrese el día (1–31): ").strip()
        if not self.validar_dia(dia_ingresado):
            print("Día inválido. Debe estar entre 1 y 31.")
            return None

        print(f"Horarios disponibles para el día {dia_ingresado}")
        self.listar_slots(dia_ingresado)

        hora_ingresada = input("Ingrese el horario (HH:MM): ").strip()
        if not self.validar_hora(hora_ingresada):
            print("Formato de hora inválido. Debe ser HH:MM (por ejemplo 09:30).")
            return None

        # Normaliza valores ingresados
        dia_normalizado = dia_ingresado.strip()
        hora_normalizada = datetime.strptime(hora_ingresada.strip(), "%H:%M").strftime("%H:%M")

        # Busca el slot correspondiente
        i = 0
        while i < len(self.slots):
            slot = self.slots[i]
            if str(slot.dia) == dia_normalizado and slot.hora == hora_normalizada:
                if slot.estado == "ocupado":
                    print("Ese horario ya está ocupado.")
                    return None

                # Marca el slot como ocupado (solo en memoria)
                slot.estado = "ocupado"
                print(f"Turno asignado: Día {slot.dia} - {slot.hora}")
                return slot
            i = i + 1

        print("No hay horarios disponibles para esa fecha.")
        return None