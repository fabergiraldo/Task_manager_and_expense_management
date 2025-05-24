from flask import Blueprint, request, jsonify
import jwt
from Utilidades.Configuracion import SECRET_KEY
from Repositorio.TransaccionesRepositorio import TransaccionesRepositorio
from Entidades.Transacciones import Transacciones
from datetime import datetime, timedelta

transacciones_controller = Blueprint('transacciones', __name__)

def verificar_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False

@transacciones_controller.route('/transacciones/token', methods=['GET'])
def obtener_token_transacciones():
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    if usuario == "admin" and password == "password123":
        token = jwt.encode({"usuario": usuario, "exp": datetime.utcnow() + timedelta(hours=1)}, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token})
    return jsonify({"error": "Credenciales inválidas"}), 401

@transacciones_controller.route('/transacciones/<accion>', methods=['GET'])
def transacciones_crud(accion):
    token = request.args.get('token')
    if not token or not verificar_token(token):
        return jsonify({"error": "Token inválido"}), 401

    if accion == 'listar':
        lst = TransaccionesRepositorio.listar()
        return jsonify([t.serialize() for t in lst])

    elif accion == 'crear':
        id_usuario     = request.args.get('id_usuario')
        tipo           = request.args.get('tipo')  # 'Ingreso' o 'Gasto'
        id_categoria   = request.args.get('id_categoria')
        id_moneda      = request.args.get('id_moneda')
        id_cuenta      = request.args.get('id_cuenta')
        id_metodo_pago = request.args.get('id_metodo_pago')
        fecha_str      = request.args.get('fecha')
        fecha          = datetime.fromisoformat(fecha_str) if fecha_str else datetime.utcnow()
        t = Transacciones(id_usuario=id_usuario, tipo=tipo, id_categoria=id_categoria,
                        id_moneda=id_moneda, id_cuenta=id_cuenta,
                        id_metodo_pago=id_metodo_pago, fecha=fecha)
        TransaccionesRepositorio.crear(t)
        return jsonify({"mensaje": "Transacción creada"})

    elif accion == 'actualizar':
        id_t           = request.args.get('id_transaccion')
        id_usuario     = request.args.get('id_usuario')
        tipo           = request.args.get('tipo')
        id_categoria   = request.args.get('id_categoria')
        id_moneda      = request.args.get('id_moneda')
        id_cuenta      = request.args.get('id_cuenta')
        id_metodo_pago = request.args.get('id_metodo_pago')
        fecha_str      = request.args.get('fecha')
        fecha          = datetime.fromisoformat(fecha_str) if fecha_str else datetime.utcnow()
        t = Transacciones(id_transaccion=id_t, id_usuario=id_usuario, tipo=tipo,
                        id_categoria=id_categoria, id_moneda=id_moneda,
                        id_cuenta=id_cuenta, id_metodo_pago=id_metodo_pago,
                        fecha=fecha)
        TransaccionesRepositorio.actualizar(t)
        return jsonify({"mensaje": "Transacción actualizada"})

    elif accion == 'eliminar':
        id_t = request.args.get('id_transaccion')
        TransaccionesRepositorio.eliminar(id_t)
        return jsonify({"mensaje": "Transacción eliminada"})

    else:
        return jsonify({"error": "Acción no válida"}), 400
