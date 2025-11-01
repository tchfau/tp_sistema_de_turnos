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
[8] Listar Clientes
[9] Listar Empleados
[0] Salir
""")
        
        opcion = input("Seleccione la opción deseada (0 - 9): ").strip()

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
            print("LISTA DE CLIENTES: ")
            if len(gestor.lista_clientes) == 0:
                print("No hay clientes cargados.")
            else:
                for cliente in gestor.lista_clientes:
                    print(cliente)
                    print("-" * 30)
        elif opcion == "9":
            print("LISTA DE EMPLEADOS: ")
            if len(gestor.lista_empleados) == 0:
                print("No hay empleados cargados.")
            else:
                for empleado in gestor.lista_empleados:
                    print(empleado) 
                    print("-" * 30)
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")