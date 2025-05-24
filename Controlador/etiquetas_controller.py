from flask import Blueprint, request, jsonify
import jwt
from Utilidades.Configuracion import SECRET_KEY
from Repositorio.EtiquetasRepositorio import EtiquetasRepositorio
from Entidades.Etiquetas import Etiquetas
from datetime import datetime, timedelta

etiquetas_controller = Blueprint('etiquetas', __name__)

def verificar_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False

@etiquetas_controller.route('/etiquetas/token', methods=['GET'])
def obtener_token_etiquetas():
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    if usuario == "admin" and password == "password123":
        token = jwt.encode({"usuario": usuario, "exp": datetime.utcnow() + timedelta(hours=1)}, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token})
    return jsonify({"error": "Credenciales inválidas"}), 401

@etiquetas_controller.route('/etiquetas/<accion>', methods=['GET'])
def etiquetas_crud(accion):
    token = request.args.get('token')
    if not token or not verificar_token(token):
        return jsonify({"error": "Token inválido"}), 401

    if accion == 'listar':
        lista = EtiquetasRepositorio.listar()
        return jsonify([e.serialize() for e in lista])
    elif accion == 'crear':
        nombre = request.args.get('nombre')
        e = Etiquetas(nombre=nombre)
        EtiquetasRepositorio.crear(e)
        return jsonify({"mensaje": "Etiqueta creada"})
    elif accion == 'actualizar':
        id_et = request.args.get('id_etiqueta')
        nombre = request.args.get('nombre')
        e = Etiquetas(id_etiqueta=id_et, nombre=nombre)
        EtiquetasRepositorio.actualizar(e)
        return jsonify({"mensaje": "Etiqueta actualizada"})
    elif accion == 'eliminar':
        id_et = request.args.get('id_etiqueta')
        EtiquetasRepositorio.eliminar(id_et)
        return jsonify({"mensaje": "Etiqueta eliminada"})
    else:
        return jsonify({"error": "Acción no válida"}), 400
