class Transformador:
    def __init__(self, campos):
        self.campos = campos

    def ingresar_valores(self):
        valores = {}
        i = 0
        while i < len(self.campos):
            campo = self.campos[i]
            valor = input(f"Ingrese {campo}: ")
            valores[campo] = valor
            i += 1
        return valores