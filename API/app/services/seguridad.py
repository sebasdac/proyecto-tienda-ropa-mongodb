from functools import wraps
from datetime import datetime, timedelta, timezone
import hmac
import jwt
from flask import current_app, request, jsonify


def generar_token():
    ahora = datetime.now(timezone.utc)
    return jwt.encode({"sub": current_app.config["API_USERNAME"], "iat": ahora, "exp": ahora + timedelta(hours=2)}, current_app.config["JWT_SECRET"], algorithm="HS256")


def token_requerido(funcion):
    @wraps(funcion)
    def protegido(*args, **kwargs):
        header = request.headers.get("Authorization", "")
        if not header.startswith("Bearer "):
            return jsonify({"error": "Se requiere Authorization: Bearer <token>"}), 401
        try:
            jwt.decode(header[7:], current_app.config["JWT_SECRET"], algorithms=["HS256"], options={"require": ["exp", "sub"]})
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token vencido"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token inválido"}), 401
        return funcion(*args, **kwargs)
    return protegido


def credenciales_validas(usuario, clave):
    return bool(current_app.config["API_USERNAME"] and current_app.config["API_PASSWORD"] and current_app.config["JWT_SECRET"] and
                hmac.compare_digest(str(usuario), current_app.config["API_USERNAME"]) and
                hmac.compare_digest(str(clave), current_app.config["API_PASSWORD"]))
