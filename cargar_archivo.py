from transformador import Transformador

def carga_archivos(nombre_archivo):
    archivo = open(nombre_archivo, "rt")
    llaves_archivo = archivo.readline()
    transformador = Transformador(llaves_archivo)  # crea el objeto con las claves para cada archivo
    lista_valores = []

    line = archivo.readline()
    while line != "":
        if line == "\n":  # saltar líneas vacías
            line = archivo.readline()
            continue
        d = transformador.str2dict(line)
        lista_valores.append(d)
        line = archivo.readline()

    archivo.close()
    return transformador, lista_valores
