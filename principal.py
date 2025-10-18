#------------ Programa principal --------------- 

def registrar_cliente():
    print("Registra nuevo cliente")

def registrar_nuevo_empleado():
    print("Registra nuevo empleado")

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
            registrar_cliente()
        elif opcion == "2":
            registrar_nuevo_empleado()
        elif opcion == "3":
            solicitar_turno()
        elif opcion == "4":
            listar_trunos()
        elif opcion == "5":
            modificar_turno()
        elif opcion == "6":
            cancelar_turno()
        elif opcion == "7":
            guardar_datos()
        elif opcion == "8":
            print("Saliendo del programa")
            break
        else:
            print("Opción inválida. Intente nuevamente")

mostrar_menu()