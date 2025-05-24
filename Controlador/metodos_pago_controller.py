from flask import Blueprint, request, jsonify
import jwt
from Utilidades.Configuracion import SECRET_KEY
from Repositorio.MetodosPagoRepositorio import MetodosPagoRepositorio
from Entidades.MetodosPago import MetodosPago
from datetime import datetime, timedelta

metodos_pago_controller = Blueprint('metodos_pago', __name__)

def verificar_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False

@metodos_pago_controller.route('/metodos_pago/token', methods=['GET'])
def obtener_token_metodos_pago():
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    if usuario == "admin" and password == "password123":
        token = jwt.encode({"usuario": usuario, "exp": datetime.utcnow() + timedelta(hours=1)}, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token})
    return jsonify({"error": "Credenciales inválidas"}), 401

@metodos_pago_controller.route('/metodos_pago/<accion>', methods=['GET'])
def metodos_pago_crud(accion):
    token = request.args.get('token')
    if not token or not verificar_token(token):
        return jsonify({"error": "Token inválido"}), 401

    if accion == 'listar':
        lista = MetodosPagoRepositorio.listar()
        return jsonify([m.serialize() for m in lista])
    elif accion == 'crear':
        metodo = request.args.get('metodo')
        m = MetodosPago(metodo=metodo)
        MetodosPagoRepositorio.crear(m)
        return jsonify({"mensaje": "Método de pago creado"})
    elif accion == 'actualizar':
        id_mp = request.args.get('id_metodo_pago')
        metodo = request.args.get('metodo')
        m = MetodosPago(id_metodo_pago=id_mp, metodo=metodo)
        MetodosPagoRepositorio.actualizar(m)
        return jsonify({"mensaje": "Método de pago actualizado"})
    elif accion == 'eliminar':
        id_mp = request.args.get('id_metodo_pago')
        MetodosPagoRepositorio.eliminar(id_mp)
        return jsonify({"mensaje": "Método de pago eliminado"})
    else:
        return jsonify({"error": "Acción no válida"}), 400
