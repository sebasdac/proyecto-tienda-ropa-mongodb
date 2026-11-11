from .comun import crear_crud
from ..models.venta import Venta

ventas_bp = crear_crud(Venta)
