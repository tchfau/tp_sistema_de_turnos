class Turno:
    def __init__(self, cliente=None, empleado=None, id_cliente=None, id_empleado=None, dia=None, hora=None, **kwargs):
        self.cliente = cliente
        self.empleado = empleado
        self.id_cliente = str(id_cliente) if id_cliente is not None else ""
        self.id_empleado = str(id_empleado) if id_empleado is not None else ""
        self.dia = str(dia) if dia is not None else ""
        self.hora = str(hora) if hora is not None else ""

        for clave in kwargs:
            setattr(self, clave, kwargs[clave])

    def mostrar(self):
        texto = "Turno:\n"

        #CLIENTE
        texto += "Cliente:\n"
        if self.cliente is not None:
            if hasattr(self.cliente, "__dict__"):
                atributos_cliente = vars(self.cliente)
                for clave in atributos_cliente:
                    valor = atributos_cliente[clave]
                    texto += "    " + str(clave) + ": " + str(valor) + "\n"
            else:
                texto += "    " + str(self.cliente) + "\n"
        elif hasattr(self, "id_cliente") and self.id_cliente != "":
            texto += "id_cliente: " + str(self.id_cliente) + "\n"
        else:
            texto += "(sin datos)\n"

        #EMPLEADO
        texto += "Empleado:\n"
        if self.empleado is not None:
            if hasattr(self.empleado, "__dict__"):
                atributos_empleado = vars(self.empleado)
                for clave in atributos_empleado:
                    valor = atributos_empleado[clave]
                    texto += "    " + str(clave) + ": " + str(valor) + "\n"
            else:
                texto += "    " + str(self.empleado) + "\n"
        elif hasattr(self, "id_empleado") and self.id_empleado != "":
            texto += "id_empleado: " + str(self.id_empleado) + "\n"
        else:
            texto += "(sin datos)\n"

        # --- DÍA Y HORA ---
        texto += "Día: " + str(self.dia) + "\n"
        texto += "Hora: " + str(self.hora)

        return texto.strip()

    def __str__(self):
        return self.mostrar()

