from transformador import Transformador

class DB(object):

    def __init__(self, filename, tipo_registro=None):
        self.filename = filename
        self.tipo_registro = tipo_registro
    
    def read(self):
        lista_valores = []
        file = open(self.filename, "rt")

        llaves_archivo = file.readline()
        if llaves_archivo == "":
            file.close()
            return None, []  # devuelve archivo vacío, sin transformador

        transformador = Transformador(llaves_archivo)

        llaves_archivo = file.readline().strip().replace(";", "")
        line = file.readline() # Leo encabezado
        while line != "":
            if line == "\n":  # saltar líneas vacías
                line = file.readline() # Leo la primera línea
                continue
            line = line.replace(';', '')
            d = transformador.str2dict(line)

            if self.tipo_registro:
                objeto = self.tipo_registro(**d)
                lista_valores.append(objeto)
            else:
                lista_valores.append(d)

            line = file.readline()

        file.close()
        return transformador, lista_valores
    

    def write(self, registros):
        pass

db_clientes = DB("clientes.csv")
registros = db_clientes.read()

"""

i = 0
while i < len(registros):
    print("Nombre: ", registros[i]["nombre"])
    i = i + 1

"""
