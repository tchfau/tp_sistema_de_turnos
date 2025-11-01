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

        line = file.readline()

        #llaves_archivo = file.readline().strip().replace(";", "")
        #line = file.readline() # Leo encabezado

        while line != "":
            line = line.strip()
            if line == "":  # ignora líneas vacías
                line = file.readline()
                continue

            line = line.replace(";", "")
            d = transformador.str2dict(line)

            # Si hay clase asociada, crea el objeto; si no, guarda el diccionario
            if self.tipo_registro:
                objeto = self.tipo_registro(**d)
                lista_valores.append(objeto)
            else:
                lista_valores.append(d)

            # Leo la siguiente línea
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
