from db import DB
from persona import Empleado

class GestorEmpleados:
    def __init__(self):
        self.db_empleados = DB("empleados.csv", Empleado)
        self.encabezado, self.lista_empleados = self.db_empleados.read()

        if self.encabezado is None:
            # Encabezado por defecto si el archivo está vacío o no existe
            self.encabezado = ["id_empleado", "nombre", "apellido", "cuil"]

        if self.lista_empleados is None:
            self.lista_empleados = []

    def registrar_empleado(self):
        #Registra un nuevo empleado en memoria.
        try:
            # Ingreso de datos por consola según el encabezado
            datos = {}
            for clave in self.encabezado:
                valor = input(f"Ingrese {clave}: ").strip()
                datos[clave] = valor

            # Crear y agregar el nuevo empleado a la lista en memoria
            nuevo_empleado = Empleado(**datos)
            self.lista_empleados.append(nuevo_empleado)

            print("Empleado registrado correctamente.")

        except Exception as e:
            print("Error al registrar empleado:", e)

    def listar_empleados(self):
        #Lista los empleados cargados (desde el archivo o en memoria).
        if not self.lista_empleados:
            print("No hay empleados registrados.")
            return

        print("\n--- LISTA DE EMPLEADOS ---")
        for empleado in self.lista_empleados:
            print(empleado)
            print("-" * 30)