import os
from flask import Flask, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
from .routes.auth import auth_bp
from .routes.reportes import reportes_bp
from .controllers.usuarios import usuarios_bp
from .controllers.marcas import marcas_bp
from .controllers.prendas import prendas_bp
from .controllers.ventas import ventas_bp


def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config["JWT_SECRET"] = os.getenv("JWT_SECRET", "")
    app.config["API_USERNAME"] = os.getenv("API_USERNAME", "")
    app.config["API_PASSWORD"] = os.getenv("API_PASSWORD", "")
    mongo = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"), serverSelectionTimeoutMS=4000)
    app.extensions["mongo_client"] = mongo
    app.extensions["mongo_db"] = mongo[os.getenv("MONGO_DB", "tiendaRopa")]
    for blueprint in (auth_bp, usuarios_bp, marcas_bp, prendas_bp, ventas_bp, reportes_bp):
        app.register_blueprint(blueprint)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Ruta no encontrada"}), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({"error": "Método HTTP no permitido"}), 405

    return app
