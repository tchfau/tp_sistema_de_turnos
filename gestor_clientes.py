from db import DB
from persona import Cliente

class GestorClientes:
    def __init__(self):
        self.db_clientes = DB("clientes.csv", Cliente)
        self.encabezado, self.lista_clientes = self.db_clientes.read()

        if self.encabezado is None:
            # Encabezado por defecto en caso de archivo vacío o ausente
            self.encabezado = ["nombre", "apellido", "telefono"]

        if self.lista_clientes is None:
            self.lista_clientes = []

    def registrar_cliente(self):
        #Registra un nuevo cliente en memoria (NO escribe en el archivo CSV).
        try:
            # Ingreso de datos por consola según el encabezado
            datos = {}
            for clave in self.encabezado:
                valor = input(f"Ingrese {clave}: ").strip()
                datos[clave] = valor

            # Crear y agregar el nuevo cliente en memoria
            nuevo_cliente = Cliente(**datos)
            self.lista_clientes.append(nuevo_cliente)

            print("Cliente registrado correctamente.")

        except Exception as e:
            print("Error al registrar cliente:", e)

    def listar_clientes(self):
        # Lista los clientes cargados (desde el archivo o en memoria).
        if not self.lista_clientes:
            print("No hay clientes registrados.")
            return

        print("\n--- LISTA DE CLIENTES ---")
        for cliente in self.lista_clientes:
            print(cliente)
            print("-" * 30)

