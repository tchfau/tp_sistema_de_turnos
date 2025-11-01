from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, **kwargs):
        # Crea dinámicamente todos los atributos según el contenido del CSV
        for clave, valor in kwargs.items():
            setattr(self, clave.strip().lower(), valor)
    
    @abstractmethod
    def mostrar(self):
        pass

class Cliente(Persona):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def mostrar(self):
        atributos = vars(self)
        texto = "Cliente:\n"
        for clave, valor in atributos.items():
            texto += f"  {clave}: {valor}\n"
        return texto.strip()
    
    def __str__(self):
        return self.mostrar()

class Empleado(Persona):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def mostrar(self):
        atributos = vars(self)
        texto = "Empleado:\n"
        for clave, valor in atributos.items():
            texto += f"  {clave}: {valor}\n"
        return texto.strip()
    
    def __str__(self):
        return self.mostrar()

