from persona import Persona, Cliente, Empleado
from transformador import Transformador
from cargar_archivo import carga_archivos

class GestorTurnos(object):

    def __init__(self):
        # CLIENTES 
        transformador, lista_valores = carga_archivos("clientes.csv")
        self.transf_cliente = transformador
        self.cliente = lista_valores     

        # EMPLEADOS 
        transformador, lista_valores = carga_archivos("empleados.csv")
        self.transf_empleado = transformador
        self.empleado = lista_valores    

        # TURNOS
        transformador, lista_valores = carga_archivos("turnos.csv")
        self.transf_turnos = transformador
        self.turnos = lista_valores  


        # LISTAS 
        self.lista_clientes = []
        self.lista_empleados = []
        self.lista_turnos = []
        
    # Métodos del gestor 
    def registrar_cliente(self):
        nuevo = self.transf_cliente.ingresar_valores()
        self.lista_clientes.append(nuevo)
        print("Cliente registrado correctamente")

    def registrar_nuevo_empleado(self):
        nuevo = self.transf_empleado.ingresar_valores()
        self.lista_empleados.append(nuevo)
        print("Empleado registrado correctamente")

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
