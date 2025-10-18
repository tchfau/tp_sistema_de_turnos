from persona import Persona, Cliente, Empleado
from transformador import Transformador

#------------ Programa principal --------------- 


archivo_clientes = open("clientes.csv", "rt")
archivo_empleados = open("empleados.csv", "rt")
llaves_clientes = archivo_clientes.readline()
llaves_empleados = archivo_empleados.readline()
cliente = Transformador(llaves_clientes)
empleado = Transformador(llaves_empleados)

lista_clientes = []
lista_empleados = []

line_cli = archivo_clientes.readline()
while line_cli != "":
    if line_cli == "\n":  # saltar si la líena está vacía
        line_cli = archivo_clientes.readline()
        continue

    d = cliente.str2dict(line_cli)
    lista_clientes.append(d)
    line_cli = archivo_clientes.readline() 


line_emp = archivo_empleados.readline()
while line_emp != "":
    if line_emp == "\n":  # saltar si la líena está vacía
        line_emp = archivo_clientes.readline()
        continue

    d = empleado.str2dict(line_emp)
    lista_empleados.append(d)
    line_emp = archivo_empleados.readline() 

archivo_clientes.close()
archivo_empleados.close()

class GestorTurno(object):

    def registrar_cliente():
        nuevo = cliente.ingresar_valores()
        lista_clientes.append(nuevo)
        print("Cliente registrado correctamente")

    def registrar_nuevo_empleado():
        nuevo = empleado.ingresar_valores()
        lista_empleados.append(nuevo)
        print("Empleado registrado correctaemente")

    def solicitar_turno():
        print("Solicitando un nuevo turno")

    def listar_trunos():
        print("Se listan los turnos")

    def modificar_turno():
        print("Se modifica turno existente")

    def cancelar_turno():
        print("Se cancela turno")

    def guardar_datos():
        print("se guardan datos en archivo CSV")



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

    def mostrar_menu():
        while True:
            opcion = input("Seleccione la opción deseada (1 - 8): ")
            if opcion == "1":
                GestorTurno.registrar_cliente()
            elif opcion == "2":
                GestorTurno.registrar_nuevo_empleado()
            elif opcion == "3":
                GestorTurno.solicitar_turno()
            elif opcion == "4":
                GestorTurno.listar_trunos()
            elif opcion == "5":
                GestorTurno.modificar_turno()
            elif opcion == "6":
                GestorTurno.cancelar_turno()
            elif opcion == "7":
                GestorTurno.guardar_datos()
            elif opcion == "8":
                print("Saliendo del programa")
                break
            else:
                print("Opción inválida. Intente nuevamente")

GestorTurno.mostrar_menu()
print("Lista de empleados:\n", lista_empleados)
print("Lista de clientes:\n", lista_clientes)