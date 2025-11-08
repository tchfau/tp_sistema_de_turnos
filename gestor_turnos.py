from persona import Persona, Cliente, Empleado
from transformador import Transformador
from turno import Turno
from db import DB
from slots import Slot, GestorSlots

class GestorTurnos(object):

    def __init__(self):
        # CLIENTES
        self.db_clientes = DB("clientes.csv", Cliente)
        self.transf_cliente, self.cliente = self.cargar_datos(self.db_clientes)

        # EMPLEADOS
        self.db_empleados = DB("empleados.csv", Empleado)
        self.transf_empleado, self.empleado = self.cargar_datos(self.db_empleados)

        # TURNOS
        self.db_turnos = DB("turnos.csv", Turno)
        self.transf_turnos, self.turnos = self.cargar_datos(self.db_turnos)

        # SLOTS DE HORARIOS
        self.db_slots = DB("slots.csv", Slot)
        self.gestor_slots = GestorSlots(self.db_slots)
        self.transf_slots, self.slots = self.cargar_datos(self.db_slots)

        # LISTAS EN MEMORIA
        self.lista_clientes = self.cliente or []
        self.lista_empleados = self.empleado or []
        self.lista_turnos = self.turnos or []

    def cargar_datos(self, db_obj):
        try:
            transformador, lista_valores = db_obj.read()
            if transformador is None:
                print(f"El archivo {db_obj.filename} está vacío o no tiene encabezado.")
                transformador = None
                lista_valores = []
        except FileNotFoundError:
            print(f"Archivo {db_obj.filename} no encontrado. Se creará estructura vacía.")
            transformador = None
            lista_valores = []
        return transformador, lista_valores

    def listar_clientes(self):
        if len(self.lista_clientes) == 0:
            print("No hay clientes cargados.")
        else:
            print("LISTA DE CLIENTES: ")
            i = 0
            while i < len(self.lista_clientes):
                cliente = self.lista_clientes[i]
                print(f"\nCliente N° {i + 1}")
                print(cliente.mostrar())
                i = i + 1

    def listar_empleados(self):
        if len(self.lista_empleados) == 0:
            print("No hay empleados cargados.")
        else:
            print("LISTA DE EMPLEADOS: ")
            i = 0
            while i < len(self.lista_empleados):
                empleado = self.lista_empleados[i]
                print(f"\nEmpleado N° {i + 1}")
                print(empleado.mostrar())
                i = i + 1
    # Métodos del gestor 
    def registrar_cliente(self):
        if self.transf_cliente:
            nuevo_dict = self.transf_cliente.ingresar_valores()  # devuelve un diccionario
            # Crea un objeto Cliente con ese diccionario
            nuevo_objeto = self.db_clientes.tipo_registro(**nuevo_dict)
            self.lista_clientes.append(nuevo_objeto)
            print("Cliente registrado correctamente.")
        else:
            print("Error: No hay archivo de cliente cargado.")

    def registrar_nuevo_empleado(self):
        if self.transf_empleado:
            nuevo_dict = self.transf_empleado.ingresar_valores()
            # Crea un objeto Empleado con ese diccionario
            nuevo_objeto = self.db_empleados.tipo_registro(**nuevo_dict)
            self.lista_empleados.append(nuevo_objeto)
            print("Empleado registrado correctamente.")
        else:
            print("Error: No hay archivo de empleado cargado.")

    def solicitar_turno(self):
        print("SOLICITAR NUEVO TURNO")

        if not self.lista_clientes:
            print("No hay clientes registrados.")
            return

        if not self.lista_empleados:
            print("No hay empleados cargados.")
            return

        # Seleccionar cliente
        print("\nSeleccione el cliente:")
        i = 0
        while i < len(self.lista_clientes):
            cliente = self.lista_clientes[i]
            print(f"[{i + 1}] {cliente.nombre} {cliente.apellido}")
            i = i + 1

        opcion_cliente = input("Ingrese el número del cliente: ").strip()
        pos_cliente = None

        try:
            pos_cliente = int(opcion_cliente)
        except Exception:
            print("Opción inválida. Debe ingresar un número.")
            return

        if pos_cliente < 1 or pos_cliente > len(self.lista_clientes):
            print("Opción fuera de rango.")
            return

        cliente = self.lista_clientes[pos_cliente - 1]

        # Seleccionar empleado
        print("\nSeleccione el empleado:")
        j = 0
        while j < len(self.lista_empleados):
            empleado = self.lista_empleados[j]
            print(f"[{j + 1}] {empleado.nombre} {empleado.apellido}")
            j = j + 1

        opcion_empleado = input("Ingrese el número del empleado: ").strip()
        pos_empleado = None

        try:
            pos_empleado = int(opcion_empleado)
        except Exception:
            print("Opción inválida. Debe ingresar un número.")
            return

        if pos_empleado < 1 or pos_empleado > len(self.lista_empleados):
            print("Opción fuera de rango.")
            return

        empleado = self.lista_empleados[pos_empleado - 1]

        # Seleccionar slot (día y horario)
        slot = self.gestor_slots.seleccionar_slot()
        if not slot:
            return

        # Crear el turno vinculado
        nuevo_turno = Turno(
            cliente=cliente,
            empleado=empleado,
            dia=slot.dia,
            hora=slot.hora
        )

        self.lista_turnos.append(nuevo_turno)
        print("\nTurno registrado correctamente:")
        print(nuevo_turno)

    def listar_turnos(self):
        if not self.lista_turnos:
            print("\nNo hay turnos registrados.")
            return

        print("\n--- LISTA DE TURNOS ---")
        i = 0
        while i < len(self.lista_turnos):
            turno = self.lista_turnos[i]
            print(f"[{i + 1}] {turno}")
            print("-" * 40)
            i = i + 1

    def modificar_turno(self):
        print("Se modifica turno existente")

    def cancelar_turno(self):
        print("Se cancela turno")

    def guardar_datos(self):
        print("se guardan datos en archivo CSV")