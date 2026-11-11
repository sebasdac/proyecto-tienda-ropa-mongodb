from .comun import crear_crud
from ..models.marca import Marca

marcas_bp = crear_crud(Marca)
