from flask import Blueprint, request, jsonify
from pymongo.errors import PyMongoError
from ..services.mongo_service import MongoService, validar_datos, validar_id
from ..services.seguridad import token_requerido


def crear_crud(modelo):
    nombre = modelo.coleccion
    bp = Blueprint(nombre, __name__, url_prefix=f"/api/v1/{nombre}")
    servicio = MongoService(modelo)

    @bp.get("")
    @token_requerido
    def listar():
        return jsonify(servicio.listar())

    @bp.get("/<identificador>")
    @token_requerido
    def obtener(identificador):
        if not validar_id(identificador):
            return jsonify({"error": "ID inválido"}), 400
        dato = servicio.obtener(identificador)
        return (jsonify(dato), 200) if dato else (jsonify({"error": "No encontrado"}), 404)

    @bp.post("")
    @token_requerido
    def crear():
        datos, error = validar_datos(modelo, request.get_json(silent=True), True)
        if error:
            return jsonify({"error": error}), 400
        return jsonify(servicio.crear(datos)), 201

    @bp.put("/<identificador>")
    @token_requerido
    def actualizar(identificador):
        if not validar_id(identificador):
            return jsonify({"error": "ID inválido"}), 400
        datos, error = validar_datos(modelo, request.get_json(silent=True), False)
        if error:
            return jsonify({"error": error}), 400
        dato = servicio.actualizar(identificador, datos)
        return (jsonify(dato), 200) if dato else (jsonify({"error": "No encontrado"}), 404)

    @bp.delete("/<identificador>")
    @token_requerido
    def eliminar(identificador):
        if not validar_id(identificador):
            return jsonify({"error": "ID inválido"}), 400
        if not servicio.eliminar(identificador):
            return jsonify({"error": "No encontrado"}), 404
        return jsonify({"mensaje": "Eliminado correctamente"})

    return bp
