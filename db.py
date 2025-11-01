from transformador import Transformador

class DB(object):

    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        lista_valores = []
        file = open(self.filename, "rt")

        llaves_archivo = file.readline()
        if llaves_archivo == "":
            file.close()
            return None, []  # devuelve archivo vacío, sin transformador

        transformador = Transformador(llaves_archivo)

        line = file.readline() # Leo encabezado
        while line != "":
            if line == "\n":  # saltar líneas vacías
                line = file.readline() # Leo la primera línea
                continue
            d = transformador.str2dict(line)
            lista_valores.append(d)
            line = file.readline()

        file.close()
        return transformador, lista_valores
    

    def write(self, registros):
        pass

db_clientes = DB("clientes.csv")
registros = db_clientes.read()
i = 0
while i < len(registros):
    print("Nombre: ", registros[i]["nombre"])
    i = i + 1


