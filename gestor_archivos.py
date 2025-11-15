class GestorArchivos:

    def __init__(self, gestor_clientes, gestor_empleados, gestor_turnos):
        self.gestor_clientes = gestor_clientes
        self.gestor_empleados = gestor_empleados
        self.gestor_turnos = gestor_turnos

    def guardar_datos(self):
        confirmar = input("¿Desea guardar los datos actuales en los archivos CSV? (S/N): ").strip().lower()
        if confirmar != "s":
            print("Operación cancelada. No se guardaron los datos.")
            return

        def leer_encabezado(path):
            #Lee solo la primera línea (encabezado) del CSV
            archivo = None
            try:
                archivo = open(path, "r", encoding="utf-8-sig")
                linea = archivo.readline().strip()
                return linea if linea else ""
            except FileNotFoundError:
                return ""
            except Exception as e:
                print(f"Error al leer encabezado de '{path}': {e}")
                return ""
            finally:
                if archivo:
                    archivo.close()

        # GUARDAR CLIENTES

        try:
            archivo_path = self.gestor_clientes.db_clientes.filename
            encabezado_clientes = leer_encabezado(archivo_path)
            if not encabezado_clientes:
                encabezado_clientes = "nombre,apellido,telefono"

            archivo_clientes = None
            try:
                archivo_clientes = open(archivo_path, "w", encoding="utf-8-sig")
                archivo_clientes.write(encabezado_clientes + "\n")

                i = 0
                while i < len(self.gestor_clientes.lista_clientes):
                    c = self.gestor_clientes.lista_clientes[i]

                    id_cliente = str(getattr(c, "id_cliente", "")).strip()
                    nombre = str(getattr(c, "nombre", "")).strip()
                    apellido = str(getattr(c, "apellido", "")).strip()
                    telefono = str(getattr(c, "telefono", "")).strip()

                    # Evita coma inicial si id_cliente está vacío
                    if id_cliente:
                        linea = f"{id_cliente},{nombre},{apellido},{telefono}\n"
                    else:
                        linea = f"{nombre},{apellido},{telefono}\n"

                    # Evita escribir líneas vacías
                    if any([nombre, apellido, telefono]):
                        archivo_clientes.write(linea)
                    i += 1

                print(f"Clientes guardados correctamente en '{archivo_path}'.")
            finally:
                if archivo_clientes:
                    archivo_clientes.close()
        except Exception as e:
            print("Error al guardar clientes:", e)


        # GUARDAR EMPLEADOS 

        try:
            archivo_path = self.gestor_empleados.db_empleados.filename
            encabezado_empleados = leer_encabezado(archivo_path)
            if not encabezado_empleados:
                encabezado_empleados = "id_empleado,nombre,apellido,cuil"

            archivo_empleados = None
            try:
                archivo_empleados = open(archivo_path, "w", encoding="utf-8-sig")
                archivo_empleados.write(encabezado_empleados + "\n")

                j = 0
                while j < len(self.gestor_empleados.lista_empleados):
                    e = self.gestor_empleados.lista_empleados[j]

                    id_empleado = str(getattr(e, "id_empleado", "")).strip()
                    nombre = str(getattr(e, "nombre", "")).strip()
                    apellido = str(getattr(e, "apellido", "")).strip()
                    cuil = str(getattr(e, "cuil", "")).strip()

                    # Si falta el id_empleado, no poner coma inicial
                    if id_empleado:
                        linea = f"{id_empleado},{nombre},{apellido},{cuil}\n"
                    else:
                        linea = f"{nombre},{apellido},{cuil}\n"

                    if any([nombre, apellido, cuil]):
                        archivo_empleados.write(linea)
                    j += 1

                print(f"Empleados guardados correctamente en '{archivo_path}'.")
            finally:
                if archivo_empleados:
                    archivo_empleados.close()
        except Exception as e:
            print("Error al guardar empleados:", e)

        # GUARDAR TURNOS
        try:
            archivo_path = self.gestor_turnos.db_turnos.filename
            encabezado_turnos = "id_empleado,nombre_cliente,apellido_cliente,dia,hora"

            # CANCELACIÓN O MODIFICACIÓN
            # reemplazar completamente el archivo
            if self.gestor_turnos.remplazar_turnos:
                turnos_finales = self.gestor_turnos.lista_turnos

            else:
                
                #SOLO AGREGAR NUEVOS TURNOS
                encabezado_existente, turnos_csv = self.gestor_turnos.db_turnos.read()
                turnos_memoria = self.gestor_turnos.lista_turnos

                turnos_finales = []

                i = 0
                while i < len(turnos_csv):
                    turnos_finales.append(turnos_csv[i])
                    i += 1

                j = 0
                while j < len(turnos_memoria):
                    turnos_finales.append(turnos_memoria[j])
                    j += 1

            # ELIMINAR DUPLICADOS
            unicos = []
            vistos = set()

            k = 0
            while k < len(turnos_finales):
                t = turnos_finales[k]
                clave = t.id_empleado + "|" + str(t.dia) + "|" + str(t.hora)
                if clave not in vistos:
                    vistos.add(clave)
                    unicos.append(t)
                k += 1

            # GUARDAR CSV
            archivo = open(archivo_path, "w", encoding="utf-8-sig")
            archivo.write(encabezado_turnos + "\n")

            p = 0
            while p < len(unicos):
                t = unicos[p]
                linea = (
                    t.id_empleado + "," +
                    t.cliente.nombre + "," +
                    t.cliente.apellido + "," +
                    t.dia + "," +
                    t.hora + "\n"
                )
                archivo.write(linea)
                p += 1

            archivo.close()

            print(f"Turnos guardados correctamente en '{archivo_path}'.")

            # RESET
            self.gestor_turnos.lista_turnos = []
            self.gestor_turnos.remplazar_turnos = False

        except Exception as e:
            print("Error al guardar turnos:", e)