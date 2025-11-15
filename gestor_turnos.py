from gestor_clientes import GestorClientes
from gestor_empleados import GestorEmpleados
from gestor_slots import GestorSlots
from turno import Turno
from db import DB
from gestor_slots import Slot

class GestorTurnos(object):
    
    def __init__(self):
        # Instancias de los gestores de clientes y empleados
        self.gestor_clientes = GestorClientes()
        self.gestor_empleados = GestorEmpleados()

        # DB de slots y gestor de slots
        self.db_slots = DB("slots.csv", Slot)
        self.gestor_slots = GestorSlots(self.db_slots)

        # DB de turnos
        self.db_turnos = DB("turnos.csv", Turno)

        # Leer turnos existentes desde el archivo (solo para listar)
        self.encabezado, turnos_leidos = self.db_turnos.read()

        if turnos_leidos:
            print(f"Se cargaron {len(turnos_leidos)} turnos desde turnos.csv")
        else:
            print("No se encontraron turnos registrados en el archivo turnos.csv")

        # Mantener la lista de turnos en memoria vacía
        self.lista_turnos = []

        # BANDERA para saber si se reemplaza el CSV o solo se agregan turnos
        self.remplazar_turnos = False


    def registrar_cliente(self):
        return self.gestor_clientes.registrar_cliente()

    def listar_clientes(self):
        return self.gestor_clientes.listar_clientes()

    def registrar_nuevo_empleado(self):
        if hasattr(self.gestor_empleados, "registrar_nuevo_empleado"):
            return self.gestor_empleados.registrar_nuevo_empleado()
        elif hasattr(self.gestor_empleados, "registrar_empleado"):
            return self.gestor_empleados.registrar_empleado()
        else:
            print("No se encontró método para registrar empleados.")

    def listar_empleados(self):
        return self.gestor_empleados.listar_empleados()

    def solicitar_turno(self):
        # Leer clientes y empleados actualizados
        encabezado_clientes, lista_clientes = self.gestor_clientes.db_clientes.read()
        encabezado_empleados, lista_empleados = self.gestor_empleados.db_empleados.read()

        self.gestor_clientes.lista_clientes = lista_clientes
        self.gestor_empleados.lista_empleados = lista_empleados

        if not lista_clientes or not lista_empleados:
            print("Debe haber al menos un cliente y un empleado registrados.")
            return

        # Selección Cliente 
        print("\nSeleccione cliente:")
        i = 0
        while i < len(lista_clientes):
            c = lista_clientes[i]
            print("[" + str(i + 1) + "] " + c.nombre + " " + c.apellido)
            i += 1

        try:
            opcion_cliente = int(input("Número de cliente: ")) - 1
            if opcion_cliente < 0 or opcion_cliente >= len(lista_clientes):
                print("Cliente inválido.")
                return
        except:
            print("Entrada inválida.")
            return

        cliente = lista_clientes[opcion_cliente]

        # Selección Empleado 
        print("\nSeleccione empleado:")
        j = 0
        while j < len(lista_empleados):
            e = lista_empleados[j]
            print("[" + str(j + 1) + "] " + e.nombre + " " + e.apellido)
            j += 1

        try:
            opcion_empleado = int(input("Número de empleado: ")) - 1
            if opcion_empleado < 0 or opcion_empleado >= len(lista_empleados):
                print("Empleado inválido.")
                return
        except:
            print("Entrada inválida.")
            return

        empleado = lista_empleados[opcion_empleado]
        id_empleado = empleado.id_empleado

        # Dia 
        try:
            dia_input = int(input("Ingrese el día (1–31): ").strip())
            if dia_input < 1 or dia_input > 31:
                print("Día inválido.")
                return
        except:
            print("Entrada inválida.")
            return

        # Turnos existentes
        encabezado_turnos, turnos_existentes = self.db_turnos.read()

        # Slot 
        slot = self.gestor_slots.seleccionar_slot_para_empleado(
            id_empleado,
            dia_input,
            turnos_existentes,
            lista_empleados
        )
        if slot is None:
            return

        # Validación
        k = 0
        while k < len(turnos_existentes):
            t = turnos_existentes[k]
            if t.id_empleado == id_empleado and str(t.dia) == str(slot.dia) and str(t.hora) == str(slot.hora):
                print("\nEl empleado ya tiene un turno registrado en ese horario.")
                return
            k += 1

        # Crear turno 
        nuevo_turno = Turno(
            cliente=cliente,
            empleado=empleado,
            id_cliente="",
            id_empleado=id_empleado,
            dia=str(slot.dia),
            hora=str(slot.hora)
        )

        self.lista_turnos.append(nuevo_turno)

        # Solicitando un turno = se están agregando turnos nuevos
        self.remplazar_turnos = False

        print("\nTurno registrado correctamente (pendiente de guardado).")
        print("Cliente:", cliente.nombre, cliente.apellido)
        print("Empleado:", empleado.nombre, empleado.apellido)
        print("Día:", slot.dia, "| Hora:", slot.hora)
        print("\nEl turno se guardará al ejecutar la opción 7 (Guardar datos).")


    def listar_turnos(self):
        encabezado_turnos, turnos = self.db_turnos.read()

        if not turnos:
            print("No hay turnos registrados.")
            return

        print("\n--- LISTA DE TURNOS ---")

        i = 0
        while i < len(turnos):
            t = turnos[i]
            print(
                f"Empleado ID: {t.id_empleado} | "
                f"Cliente: {t.cliente.nombre} {t.cliente.apellido} | "
                f"Día: {t.dia} | Hora: {t.hora}"
            )
            i += 1

        print("----------------------------------------")

    def cancelar_turno(self):
        encabezado_turnos, turnos = self.db_turnos.read()

        if not turnos:
            print("No hay turnos registrados para cancelar.")
            return

        print("\n--- TURNOS REGISTRADOS ---")

        i = 0
        while i < len(turnos):
            t = turnos[i]
            print(f"[{i + 1}] Empleado ID: {t.id_empleado} | Cliente: {t.cliente.nombre} {t.cliente.apellido} | Día: {t.dia} | Hora: {t.hora}")
            i += 1

        try:
            opcion = int(input("\nIngrese el número del turno que desea cancelar: ").strip())
            if opcion < 1 or opcion > len(turnos):
                print("Opción fuera de rango.")
                return
        except:
            print("Entrada inválida.")
            return

        t = turnos[opcion - 1]

        print("\nConfirmar cancelación:")
        print(f"Empleado ID: {t.id_empleado} | Cliente: {t.cliente.nombre} {t.cliente.apellido} | Día: {t.dia} | Hora: {t.hora}")

        confirmar = input("¿Cancelar turno? (S/N): ").strip().lower()
        if confirmar != "s":
            print("Operación cancelada.")
            return

        del turnos[opcion - 1]

        # Se guardan en memoria para reemplazar el CSV
        self.lista_turnos = turnos

        # Cancelando turno: reemplazar todos los turnos existentes
        self.remplazar_turnos = True

        print("\nTurno cancelado correctamente.")
        print("Recuerde ejecutar [7] Guardar Datos para aplicar cambios.")

    def modificar_turno(self):
        # Leer turnos actuales del archivo
        encabezado_turnos, turnos = self.db_turnos.read()

        if not turnos:
            print("No hay turnos registrados para modificar.")
            return

        print("\n--- TURNOS REGISTRADOS ---")

        i = 0
        while i < len(turnos):
            t = turnos[i]
            print(
                "[" + str(i + 1) + "] "
                "Empleado ID: " + str(t.id_empleado) +
                " | Cliente: " + t.cliente.nombre + " " + t.cliente.apellido +
                " | Día: " + str(t.dia) +
                " | Hora: " + str(t.hora)
            )
            i += 1

        # Selección del turno a modificar
        try:
            opcion = int(input("\nSeleccione el número del turno a modificar: ").strip())
            if opcion < 1 or opcion > len(turnos):
                print("Opción fuera de rango.")
                return
        except:
            print("Entrada inválida.")
            return

        turno_original = turnos[opcion - 1]

        print("\nModificar turno del cliente:",
            turno_original.cliente.nombre,
            turno_original.cliente.apellido)

        # Solicitar nuevo día
        try:
            nuevo_dia = int(input("Ingrese el nuevo día (1–31): ").strip())
            if nuevo_dia < 1 or nuevo_dia > 31:
                print("Día inválido.")
                return
        except:
            print("Entrada inválida.")
            return

        # Leer turnos existentes nuevamente para validación
        encabezado_existentes, turnos_existentes = self.db_turnos.read()

        empleado_id = turno_original.id_empleado

        # Cargar slots 
        encabezado_slots, slots = self.db_slots.read()
        if not slots:
            print("No hay slots cargados.")
            return

        lista_horas_disponibles = []

        y = 0
        while y < len(slots):
            s = slots[y]

            dia_slot = str(getattr(s, "dia", "")).strip()
            hora_slot = str(getattr(s, "hora", "")).strip()

            # El slot debe coincidir con el nuevo día
            if dia_slot != str(nuevo_dia):
                y += 1
                continue

            # Verificar si el empleado YA tiene ese turno ocupado
            ocupado = False
            k = 0
            while k < len(turnos_existentes):
                t2 = turnos_existentes[k]
                if (
                    str(t2.id_empleado) == str(empleado_id)
                    and str(t2.dia) == str(nuevo_dia)
                    and str(t2.hora) == hora_slot
                ):
                    ocupado = True
                    break
                k += 1

            if not ocupado:
                # evitar duplicados
                m = 0
                repetido = False
                while m < len(lista_horas_disponibles):
                    if lista_horas_disponibles[m] == hora_slot:
                        repetido = True
                        break
                    m += 1
                if not repetido:
                    lista_horas_disponibles.append(hora_slot)

            y += 1

        if not lista_horas_disponibles:
            print("No hay horarios disponibles para ese empleado en ese día.")
            return

        print("\nSeleccione nueva hora para el turno:")
        z = 0
        while z < len(lista_horas_disponibles):
            print("[" + str(z + 1) + "] Hora:", lista_horas_disponibles[z])
            z += 1

        entrada = input("Seleccione el número de la hora o escriba la hora (ej: 14:00): ").strip()

        nueva_hora = None

        # Si la entrada es un número, interpretarlo como índice
        es_numero = True
        try:
            _test = int(entrada)
        except:
            es_numero = False

        if es_numero:
            num = int(entrada)
            if num >= 1 and num <= len(lista_horas_disponibles):
                nueva_hora = lista_horas_disponibles[num - 1]
            else:
                print("Opción de hora inválida.")
                return

        else:
            # Si la entrada es una hora, buscarla dentro de la lista
            h = entrada
            w = 0
            encontrada = False
            while w < len(lista_horas_disponibles):
                if lista_horas_disponibles[w] == h:
                    nueva_hora = h
                    encontrada = True
                    break
                w += 1

            if not encontrada:
                print("La hora ingresada no está disponible.")
                return

        # Confirmación
        print("\nConfirmar modificación del turno:")
        print("Empleado ID:", empleado_id)
        print("Cliente:", turno_original.cliente.nombre, turno_original.cliente.apellido)
        print("Nuevo día:", nuevo_dia)
        print("Nueva hora:", nueva_hora)

        confirmar = input("¿Modificar turno? (S/N): ").strip().lower()
        if confirmar != "s":
            print("Operación cancelada.")
            return

        # Aplicar modificación en memoria
        turno_original.dia = str(nuevo_dia)
        turno_original.hora = str(nueva_hora)

        # El archivo debe reescribirse completamente
        self.lista_turnos = turnos
        self.remplazar_turnos = True

        print("\nTurno modificado correctamente.")
        print("Recuerde ejecutar [7] Guardar Datos para aplicar cambios.")