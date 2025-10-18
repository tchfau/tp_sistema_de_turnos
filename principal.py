from persona import Persona, Cliente, Empleado
from transformador import Transformador

#------------ Programa principal --------------- 

class GestorTurnos(object):

    def __init__(self):
        # Carga y lectura de l archivo clientes
        archivo_clientes = open("clientes.csv", "rt")
        llaves_clientes = archivo_clientes.readline()
        self.cliente = Transformador(llaves_clientes)
        self.lista_clientes = []

        line_cli = archivo_clientes.readline()
        while line_cli != "":
            if line_cli == "\n":  # saltar si la línea está vacía
                line_cli = archivo_clientes.readline()
                continue
            d = self.cliente.str2dict(line_cli)
            self.lista_clientes.append(d)
            line_cli = archivo_clientes.readline()
        archivo_clientes.close()

        # Carga y lectura del archivo empleados
        archivo_empleados = open("empleados.csv", "rt")
        llaves_empleados = archivo_empleados.readline()
        self.empleado = Transformador(llaves_empleados)
        self.lista_empleados = []

        line_emp = archivo_empleados.readline()
        while line_emp != "":
            if line_emp == "\n":  # saltar si la línea está vacía
                line_emp = archivo_empleados.readline()
                continue
            d = self.empleado.str2dict(line_emp)
            self.lista_empleados.append(d)
            line_emp = archivo_empleados.readline()
        archivo_empleados.close()

    # Métodos del gestor 
    def registrar_cliente(self):
        nuevo = self.cliente.ingresar_valores()
        self.lista_clientes.append(nuevo)
        print("Cliente registrado correctamente")

    def registrar_nuevo_empleado(self):
        nuevo = self.empleado.ingresar_valores()
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

    # Menú interactivo
    def mostrar_menu(self):
        print("**************************************")
        print("**************************************")
        print('SISTEMA DE GESTIÓN DE TURNOS')
        print("**************************************")
        print("--------------------------------------")
        print("MENU PRINCIPAL")
        print("--------------------------------------")

        menu = """
[1] Registrar nuevo Cliente
[2] Registrar nuevo Empleado
[3] Solicitar turno
[4] Listar turnos existentes
[5] Modificar turno
[6] Cancelar turno
[7] Guardar datos 
[8] Salir
"""
        print(menu)

        while True:
            opcion = input("Seleccione la opción deseada (1 - 8): ")
            if opcion == "1":
                self.registrar_cliente()
            elif opcion == "2":
                self.registrar_nuevo_empleado()
            elif opcion == "3":
                self.solicitar_turno()
            elif opcion == "4":
                self.listar_turnos()
            elif opcion == "5":
                self.modificar_turno()
            elif opcion == "6":
                self.cancelar_turno()
            elif opcion == "7":
                self.guardar_datos()
            elif opcion == "8":
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida. Intente nuevamente.")

        print("Lista de empleados:\n", self.lista_empleados)
        print("Lista de clientes:\n", self.lista_clientes)


# Ejecución del programa
gestor = GestorTurnos()
gestor.mostrar_menu()