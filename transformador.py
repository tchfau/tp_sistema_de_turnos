class Transformador(object):
    def __init__(self, keys):
        self.keys = keys.replace("\n", "").split(",")  # se elimina el salto de línea
        

    def str2dict(self, valores):
        fila = valores.replace("\n", "").split(",") 
        d = {}
        j = 0
        while j < len(self.keys) and j < len(fila):
            d[self.keys[j]] = fila[j]
            j = j + 1
        return d
    
    def ingresar_valores(self):
        #Permite ingresar valores desde teclado y genera un diccionario nuevo
        print("Ingrese los valores para las siguientes claves:")
        fila = []
        j = 0
        while j < len(self.keys):
            valor = input(f"{self.keys[j]}: ")
            fila.append(valor)
            j = j + 1
        valores = ",".join(fila)
        return self.str2dict(valores)

