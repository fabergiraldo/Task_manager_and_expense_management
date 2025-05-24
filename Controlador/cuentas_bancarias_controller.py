from flask import Blueprint, request, jsonify
import jwt
from Utilidades.Configuracion import SECRET_KEY
from Repositorio.CuentasBancariasRepositorio import CuentasBancariasRepositorio
from Entidades.CuentasBancarias import CuentasBancarias
from datetime import datetime, timedelta

cuentas_bancarias_controller = Blueprint('cuentas_bancarias', __name__)

def verificar_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False

@cuentas_bancarias_controller.route('/cuentas_bancarias/token', methods=['GET'])
def obtener_token_cuentas():
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    if usuario == "admin" and password == "password123":
        token = jwt.encode(
            {"usuario": usuario, "exp": datetime.utcnow() + timedelta(hours=1)},
            SECRET_KEY, algorithm="HS256"
        )
        return jsonify({"token": token})
    return jsonify({"error": "Credenciales inválidas"}), 401

@cuentas_bancarias_controller.route('/cuentas_bancarias/<accion>', methods=['GET'])
def cuentas_bancarias_crud(accion):
    token = request.args.get('token')
    if not token or not verificar_token(token):
        return jsonify({"error": "Token inválido"}), 401

    if accion == 'listar':
        lista = CuentasBancariasRepositorio.listar()
        return jsonify([c.serialize() for c in lista])
    elif accion == 'crear':
        id_usuario    = request.args.get('id_usuario')
        nombre_banco  = request.args.get('nombre_banco')
        numero_cuenta = request.args.get('numero_cuenta')
        saldo         = request.args.get('saldo')
        id_moneda     = request.args.get('id_moneda')
        c = CuentasBancarias(id_usuario=id_usuario, nombre_banco=nombre_banco,
                           numero_cuenta=numero_cuenta, saldo=saldo, id_moneda=id_moneda)
        CuentasBancariasRepositorio.crear(c)
        return jsonify({"mensaje": "Cuenta bancaria creada"})
    elif accion == 'actualizar':
        id_cuenta     = request.args.get('id_cuenta')
        id_usuario    = request.args.get('id_usuario')
        nombre_banco  = request.args.get('nombre_banco')
        numero_cuenta = request.args.get('numero_cuenta')
        saldo         = request.args.get('saldo')
        id_moneda     = request.args.get('id_moneda')
        c = CuentasBancarias(id_cuenta=id_cuenta, id_usuario=id_usuario,
                           nombre_banco=nombre_banco, numero_cuenta=numero_cuenta,
                           saldo=saldo, id_moneda=id_moneda)
        CuentasBancariasRepositorio.actualizar(c)
        return jsonify({"mensaje": "Cuenta bancaria actualizada"})
    elif accion == 'eliminar':
        id_cuenta = request.args.get('id_cuenta')
        CuentasBancariasRepositorio.eliminar(id_cuenta)
        return jsonify({"mensaje": "Cuenta bancaria eliminada"})
    else:
        return jsonify({"error": "Acción no válida"}), 400
