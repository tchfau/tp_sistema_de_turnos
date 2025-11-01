class Turno(object):
    def __init__(self, **kwargs):
        for clave, valor in kwargs.items():
            setattr(self, clave.strip().lower(), valor)

    def mostrar(self):
        atributos = vars(self)
        texto = "Turno:\n"
        for clave, valor in atributos.items():
            texto += f"  {clave}: {valor}\n"
        return texto.strip()

    def __str__(self):
        return self.mostrar()
