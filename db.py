from persona import Cliente, Empleado
from turno import Turno

class DB(object):
    def __init__(self, filename, tipo_registro=None):
        self.filename = filename
        self.tipo_registro = tipo_registro

    def read(self):
        try:
            archivo = open(self.filename, "r", encoding="utf-8-sig")
            lineas = archivo.readlines()
            archivo.close()
        except FileNotFoundError:
            return None, []
        except Exception:
            return None, []

        if not lineas:
            return None, []

        # Encabezado
        encabezado = lineas[0].strip().replace("\ufeff", "").split(",")

        lista = []

        i = 1
        while i < len(lineas):
            linea = lineas[i].strip()
            i += 1

            if not linea:
                continue

            partes = linea.split(",")

            # NORMALIZACIÓN TURNOS
            if self.tipo_registro and self.tipo_registro.__name__.lower() == "turno":
                if len(partes) >= 5:
                    id_empleado = partes[0].strip()
                    nombre_cliente = partes[1].strip()
                    apellido_cliente = partes[2].strip()
                    dia = partes[3].strip()
                    hora = partes[4].strip()

                    cliente = Cliente(nombre=nombre_cliente, apellido=apellido_cliente)
                    empleado = Empleado(id_empleado=id_empleado)

                    turno = Turno(
                        cliente=cliente,
                        empleado=empleado,
                        id_empleado=id_empleado,
                        id_cliente="",
                        dia=dia,
                        hora=hora
                    )
                    lista.append(turno)
                continue

            # Para clientes/empleados
            datos = {}
            j = 0
            limite = len(encabezado)
            if len(partes) < limite:
                limite = len(partes)

            while j < limite:
                clave = encabezado[j]
                valor = partes[j].strip()
                datos[clave] = valor
                j += 1

            if self.tipo_registro:
                try:
                    obj = self.tipo_registro(**datos)
                    lista.append(obj)
                except Exception:
                    lista.append(datos)
            else:
                lista.append(datos)

        return encabezado, lista