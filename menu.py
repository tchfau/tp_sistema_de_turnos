from gestor_turnos import GestorTurnos

def mostrar_menu(gestor: GestorTurnos):
    while True:
        print("\n**************************************")
        print("******** SISTEMA DE GESTIÓN DE TURNOS ********")
        print("**************************************")
        print("--------------------------------------")
        print("MENU PRINCIPAL")
        print("--------------------------------------")
        print("""
[1] Registrar nuevo Cliente
[2] Registrar nuevo Empleado
[3] Solicitar turno
[4] Listar turnos existentes
[5] Modificar turno
[6] Cancelar turno
[7] Guardar datos 
[8] Salir
""")
        
        opcion = input("Seleccione la opción deseada (1 - 8): ").strip()

        if opcion == "1":
            gestor.registrar_cliente()
        elif opcion == "2":
            gestor.registrar_nuevo_empleado()
        elif opcion == "3":
            gestor.solicitar_turno()
        elif opcion == "4":
            gestor.listar_turnos()
        elif opcion == "5":
            gestor.modificar_turno()
        elif opcion == "6":
            gestor.cancelar_turno()
        elif opcion == "7":
            gestor.guardar_datos()
        elif opcion == "8":
            print("Saliendo del programa.")
            print("Lista de clientes:\n", gestor.lista_clientes)
            print("Lista de empleados:\n", gestor.lista_empleados)
            break
        else:
            print("Opción inválida. Intente nuevamente.")