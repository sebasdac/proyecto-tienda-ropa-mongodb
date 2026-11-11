from .comun import crear_crud
from ..models.prenda import Prenda

prendas_bp = crear_crud(Prenda)
