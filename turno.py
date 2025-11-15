class Turno:
    def __init__(self, cliente=None, empleado=None, id_cliente=None, id_empleado=None, dia=None, hora=None, **kwargs):
        self.cliente = cliente
        self.empleado = empleado
        self.id_cliente = id_cliente or ""
        self.id_empleado = id_empleado or ""
        self.dia = dia or ""
        self.hora = hora or ""

    def mostrar(self):
        texto = "Turno:\n"

        texto += "Cliente:\n"
        if self.cliente:
            texto += f"{self.cliente.mostrar()}\n"
        elif self.id_cliente:
            texto += f"  id_cliente: {self.id_cliente}\n"
        else:
            texto += "  (sin datos)\n"

        texto += "Empleado:\n"
        if self.empleado:
            texto += f"{self.empleado.mostrar()}\n"
        elif self.id_empleado:
            texto += f"  id_empleado: {self.id_empleado}\n"
        else:
            texto += "  (sin datos)\n"

        texto += f"Día: {self.dia}\nHora: {self.hora}"
        return texto.strip()

