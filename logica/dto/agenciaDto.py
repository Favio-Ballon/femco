from typing import NamedTuple


class AgenciaDto(NamedTuple):
    id: int
    direccion: str
    telefono: str
    nombre: str

    def __str__(self):
        return f'id_agencia: {self.id}, nombre: {self.nombre}, direccion: {self.direccion}, telefono: {self.telefono}'
