from flask import Blueprint, jsonify
from ..services.seguridad import token_requerido
from ..services.mongo_service import db, normalizar

reportes_bp = Blueprint("reportes", __name__, url_prefix="/api/v1/reportes")

@reportes_bp.get("/marcas-con-ventas")
@token_requerido
def marcas_con_ventas():
    pipeline = [{"$group": {"_id": "$marca"}}, {"$sort": {"_id": 1}}, {"$project": {"_id": 0, "marca": "$_id"}}]
    return jsonify(normalizar(list(db().ventas.aggregate(pipeline))))

@reportes_bp.get("/prendas-vendidas-stock")
@token_requerido
def prendas_vendidas_stock():
    pipeline = [
        {"$group": {"_id": "$producto", "cantidadVendida": {"$sum": "$cantidad"}}},
        {"$lookup": {"from": "prendas", "localField": "_id", "foreignField": "nombre", "as": "datosPrenda"}},
        {"$unwind": "$datosPrenda"},
        {"$project": {"_id": 0, "prenda": "$_id", "cantidadVendida": 1, "stockRestante": {"$subtract": ["$datosPrenda.stock", "$cantidadVendida"]}}}
    ]
    return jsonify(normalizar(list(db().ventas.aggregate(pipeline))))

@reportes_bp.get("/top-5-marcas")
@token_requerido
def top_cinco_marcas():
    pipeline = [
        {"$group": {"_id": "$marca", "cantidadVendida": {"$sum": "$cantidad"}}},
        {"$sort": {"cantidadVendida": -1}},
        {"$limit": 5},
        {"$project": {"_id": 0, "marca": "$_id", "cantidadVendida": 1}}
    ]
    return jsonify(normalizar(list(db().ventas.aggregate(pipeline))))
