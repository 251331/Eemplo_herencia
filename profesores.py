# profesores.py
from persona import Persona

class Profesores(Persona):
    def __init__(self):
        super().__init__()
        self._departamento = ""
        self._categoria = ""
        self._maximoGrado = ""

    # Getter y Setter
    def get_departamento(self):
        return self._departamento

    def set_departamento(self, departamento):
        self._departamento = departamento

    def get_categoria(self):
        return self._categoria

    def set_categoria(self, categoria):
        self._categoria = categoria

    def get_maximoGrado(self):
        return self._maximoGrado

    def set_maximoGrado(self, maximoGrado):
        self._maximoGrado = maximoGrado

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Departamento: {self._departamento}, Categoria: {self._categoria}, Maximo Grado de Estudios: {self._maximoGrado}"
