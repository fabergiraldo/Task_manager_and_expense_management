from flask import Blueprint, request, jsonify
import jwt
from Utilidades.Configuracion import SECRET_KEY
from Repositorio.MonedasRepositorio import MonedasRepositorio
from Entidades.Monedas import Monedas
from datetime import datetime, timedelta

monedas_controller = Blueprint('monedas', __name__)

def verificar_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False

@monedas_controller.route('/monedas/token', methods=['GET'])
def obtener_token_monedas():
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    if usuario == "admin" and password == "password123":
        token = jwt.encode(
            {"usuario": usuario, "exp": datetime.utcnow() + timedelta(hours=1)},
            SECRET_KEY, algorithm="HS256"
        )
        return jsonify({"token": token})
    return jsonify({"error": "Credenciales inválidas"}), 401

@monedas_controller.route('/monedas/<accion>', methods=['GET'])
def monedas_crud(accion):
    token = request.args.get('token')
    if not token or not verificar_token(token):
        return jsonify({"error": "Token inválido"}), 401

    if accion == 'listar':
        lista = MonedasRepositorio.listar()
        return jsonify([m.serialize() for m in lista])
    elif accion == 'crear':
        nombre = request.args.get('nombre')
        codigo = request.args.get('codigo')
        simbolo = request.args.get('simbolo')
        m = Monedas(nombre=nombre, codigo=codigo, simbolo=simbolo)
        MonedasRepositorio.crear(m)
        return jsonify({"mensaje": "Moneda creada"})
    elif accion == 'actualizar':
        id_m = request.args.get('id_moneda')
        nombre = request.args.get('nombre')
        codigo = request.args.get('codigo')
        simbolo = request.args.get('simbolo')
        m = Monedas(id_moneda=id_m, nombre=nombre, codigo=codigo, simbolo=simbolo)
        MonedasRepositorio.actualizar(m)
        return jsonify({"mensaje": "Moneda actualizada"})
    elif accion == 'eliminar':
        id_m = request.args.get('id_moneda')
        MonedasRepositorio.eliminar(id_m)
        return jsonify({"mensaje": "Moneda eliminada"})
    else:
        return jsonify({"error": "Acción no válida"}), 400