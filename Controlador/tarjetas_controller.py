from flask import Blueprint, request, jsonify
import jwt
from Utilidades.Configuracion import SECRET_KEY
from Repositorio.TarjetasRepositorio import TarjetasRepositorio
from Entidades.Tarjetas import Tarjetas
from datetime import datetime, timedelta

tarjetas_controller = Blueprint('tarjetas', __name__)

def verificar_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False

@tarjetas_controller.route('/tarjetas/token', methods=['GET'])
def obtener_token_tarjetas():
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    if usuario == "admin" and password == "password123":
        token = jwt.encode(
            {"usuario": usuario, "exp": datetime.utcnow() + timedelta(hours=1)},
            SECRET_KEY, algorithm="HS256"
        )
        return jsonify({"token": token})
    return jsonify({"error": "Credenciales inválidas"}), 401

@tarjetas_controller.route('/tarjetas/<accion>', methods=['GET'])
def tarjetas_crud(accion):
    token = request.args.get('token')
    if not token or not verificar_token(token):
        return jsonify({"error": "Token inválido"}), 401

    if accion == 'listar':
        lista = TarjetasRepositorio.listar()
        return jsonify([t.serialize() for t in lista])
    elif accion == 'crear':
        id_usuario     = request.args.get('id_usuario')
        nombre_tarjeta = request.args.get('nombre_tarjeta')
        tipo           = request.args.get('tipo')
        numero_tarjeta = request.args.get('numero_tarjeta')
        vencimiento_str= request.args.get('vencimiento')  # YYYY-MM-DD
        vencimiento    = datetime.fromisoformat(vencimiento_str).date() if vencimiento_str else None
        t = Tarjetas(id_usuario=id_usuario, nombre_tarjeta=nombre_tarjeta,
                    tipo=tipo, numero_tarjeta=numero_tarjeta, vencimiento=vencimiento)
        TarjetasRepositorio.crear(t)
        return jsonify({"mensaje": "Tarjeta creada"})
    elif accion == 'actualizar':
        id_t           = request.args.get('id_tarjeta')
        id_usuario     = request.args.get('id_usuario')
        nombre_tarjeta = request.args.get('nombre_tarjeta')
        tipo           = request.args.get('tipo')
        numero_tarjeta = request.args.get('numero_tarjeta')
        vencimiento_str= request.args.get('vencimiento')
        vencimiento    = datetime.fromisoformat(vencimiento_str).date() if vencimiento_str else None
        t = Tarjetas(id_tarjeta=id_t, id_usuario=id_usuario, nombre_tarjeta=nombre_tarjeta,
                    tipo=tipo, numero_tarjeta=numero_tarjeta, vencimiento=vencimiento)
        TarjetasRepositorio.actualizar(t)
        return jsonify({"mensaje": "Tarjeta actualizada"})
    elif accion == 'eliminar':
        id_t = request.args.get('id_tarjeta')
        TarjetasRepositorio.eliminar(id_t)
        return jsonify({"mensaje": "Tarjeta eliminada"})
    else:
        return jsonify({"error": "Acción no válida"}), 400
