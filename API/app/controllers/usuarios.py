from .comun import crear_crud
from ..models.usuario import Usuario

usuarios_bp = crear_crud(Usuario)
