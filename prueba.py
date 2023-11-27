from logica.dao import clienteDao, agenciaDao
from logica.dto.clienteDto import ClienteDto
from logica.dto.agenciaDto import AgenciaDto

for record in agenciaDao.get_all():
    print(record[3])




