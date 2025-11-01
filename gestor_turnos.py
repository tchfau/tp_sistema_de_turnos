from persona import Persona, Cliente, Empleado
from transformador import Transformador
from cargar_archivo import carga_archivos
from db import DB

class GestorTurnos(object):

    def __init__(self):
        
        # Se utilizan objetos DB para 
        #CLIENTES
        self.db_clientes = DB("clientes.csv")
        self.transf_cliente, self.cliente = self.cargar_datos(self.db_clientes)

        #EMPLEADOS
        self.db_empleados = DB("empleados.csv")
        self.transf_empleado, self.empleado = self.cargar_datos(self.db_empleados)

        #TURNOS
        self.db_turnos = DB("turnos.csv")
        self.transf_turnos, self.turnos = self.cargar_datos(self.db_turnos)


        # LISTAS DONDE SE ALMACENAN LOS OBJETOS EN MEMORIA
        self.lista_clientes = []
        self.lista_empleados = []
        self.lista_turnos = []

        #Agrega exepción de errores para la carga y verificación de archivos
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
        
    # Métodos del gestor 
    def registrar_cliente(self):
        if self.transf_cliente:
            nuevo = self.transf_cliente.ingresar_valores()
            self.lista_clientes.append(nuevo)
            print("Cliente registrado correctamente")
        else:
            print("Error: No hay archivo de cliente cargado.")

    def registrar_nuevo_empleado(self):
        if self.transf_empleado:
            nuevo = self.transf_empleado.ingresar_valores()
            self.lista_empleados.append(nuevo)
            print("Empleado registrado correctamente")
        else:
            print("Error: No hay archivo de empleado cargad.")

    def solicitar_turno(self):
        print("Solicitando un nuevo turno")

    def listar_turnos(self):
        print("Se listan los turnos")

    def modificar_turno(self):
        print("Se modifica turno existente")

    def cancelar_turno(self):
        print("Se cancela turno")

    def guardar_datos(self):
        print("se guardan datos en archivo CSV")
