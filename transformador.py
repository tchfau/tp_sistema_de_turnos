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

archivo = open("clientes.csv", "rt")
llaves = archivo.readline()
o = Transformador(llaves)

lista = []

line = archivo.readline()
while line != "":
    if line == "\n":  # saltar si la líena está vacía
        line = archivo.readline()
        continue

    d = o.str2dict(line)
    lista.append(d)

    line = archivo.readline() 

archivo.close()

print(lista)