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

        # HORARIOS DUEÑO 
        transformador, lista_valores = carga_archivos("horarios_nov_duenio.csv")
        self.transf_duenio = transformador
        self.horarios_duenio = lista_valores  

        # HORARIOS EMPLEADO
        transformador, lista_valores = carga_archivos("horarios_nov_empleado.csv")
        self.transf_empleado_horario = transformador
        self.horarios_empleado = lista_valores

        # LISTAS 
        self.lista_clientes = []
        self.lista_empleados = []
        
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
