from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    @abstractmethod
    def mostrar(self):
        pass

class Cliente(Persona):
    def __init__(self, nombre, apellido, telefono):
        super().__init__(nombre, apellido)
        self.telefono = telefono

class Empleado(Persona):
    def __init__(self, nombre, apellido, cuil):
        super().__init__(nombre, apellido)
        self.cuil = cuil

