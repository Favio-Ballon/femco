#generate builder
from typing import NamedTuple


class ClienteDto(NamedTuple):
    ci_nit: int
    nombre: str
    apellido: str
    correo: str
    telefono: str

    def __str__(self):
        return f'ci_nit: {self.ci_nit}, nombre: {self.nombre}, apellido: {self.apellido}, correo: {self.correo}, telefono: {self.telefono}'