from flask import Blueprint, request, jsonify
from ..services.seguridad import generar_token, credenciales_validas

auth_bp = Blueprint("auth", __name__, url_prefix="/api/v1")

@auth_bp.post("/login")
def login():
    datos = request.get_json(silent=True) or {}
    if not isinstance(datos, dict):
        return jsonify({"error": "Envía un objeto JSON"}), 400
    if not credenciales_validas(datos.get("usuario", ""), datos.get("contrasena", "")):
        return jsonify({"error": "Credenciales incorrectas o sin configurar"}), 401
    return jsonify({"access_token": generar_token(), "token_type": "Bearer", "expires_in": 7200})
