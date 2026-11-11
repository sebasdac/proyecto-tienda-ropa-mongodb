from datetime import datetime
from bson import ObjectId
from bson.errors import InvalidId
from flask import current_app
from pymongo.errors import PyMongoError


def db():
    return current_app.extensions["mongo_db"]


def normalizar(documento):
    if isinstance(documento, list):
        return [normalizar(valor) for valor in documento]
    if isinstance(documento, dict):
        return {clave: normalizar(valor) for clave, valor in documento.items()}
    if isinstance(documento, ObjectId):
        return str(documento)
    if isinstance(documento, datetime):
        return documento.isoformat()
    return documento


def validar_id(id_texto):
    try:
        return ObjectId(id_texto)
    except (InvalidId, TypeError):
        return None


def validar_datos(modelo, datos, crear):
    if not isinstance(datos, dict):
        return None, "Envía un objeto JSON"
    if not datos:
        return None, "Debes enviar al menos un campo"
    desconocidos = set(datos) - set(modelo.campos)
    if desconocidos:
        return None, "Campos no permitidos: " + ", ".join(sorted(desconocidos))
    if crear:
        faltantes = [campo for campo in modelo.requeridos if campo not in datos]
        if faltantes:
            return None, "Faltan campos: " + ", ".join(faltantes)
    if "fecha" in datos:
        try:
            datos["fecha"] = datetime.fromisoformat(datos["fecha"].replace("Z", "+00:00"))
        except (AttributeError, ValueError):
            return None, "La fecha debe tener formato YYYY-MM-DD"
    for campo in ("precio", "total"):
        if campo in datos and (not isinstance(datos[campo], (int, float)) or isinstance(datos[campo], bool) or datos[campo] < 0):
            return None, f"{campo} debe ser numérico y no negativo"
    for campo in ("cantidad", "stock"):
        if campo in datos and (type(datos[campo]) is not int or datos[campo] < (1 if campo == "cantidad" else 0)):
            return None, f"{campo} debe ser entero positivo" if campo == "cantidad" else "stock debe ser entero no negativo"
    return datos, None


class MongoService:
    def __init__(self, modelo):
        self.modelo = modelo

    @property
    def coleccion(self):
        return db()[self.modelo.coleccion]

    def listar(self):
        return normalizar(list(self.coleccion.find()))

    def obtener(self, identificador):
        oid = validar_id(identificador)
        return normalizar(self.coleccion.find_one({"_id": oid})) if oid else None

    def crear(self, datos):
        resultado = self.coleccion.insert_one(datos)
        return self.obtener(str(resultado.inserted_id))

    def actualizar(self, identificador, datos):
        oid = validar_id(identificador)
        if oid is None:
            return None
        resultado = self.coleccion.update_one({"_id": oid}, {"$set": datos})
        return self.obtener(identificador) if resultado.matched_count else None

    def eliminar(self, identificador):
        oid = validar_id(identificador)
        return bool(oid and self.coleccion.delete_one({"_id": oid}).deleted_count)
