from flask import Blueprint, request, jsonify
import jwt
from Utilidades.Configuracion import SECRET_KEY
from Repositorio.IngresosRepositorio import IngresosRepositorio
from Entidades.Ingresos import Ingresos
from datetime import datetime, timedelta

ingresos_controller = Blueprint('ingresos', __name__)

def verificar_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False

@ingresos_controller.route('/ingresos/token', methods=['GET'])
def obtener_token_ingresos():
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    if usuario == "admin" and password == "password123":
        token = jwt.encode({"usuario": usuario, "exp": datetime.utcnow() + timedelta(hours=1)}, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token})
    return jsonify({"error": "Credenciales inválidas"}), 401

@ingresos_controller.route('/ingresos/<accion>', methods=['GET'])
def ingresos_crud(accion):
    token = request.args.get('token')
    if not token or not verificar_token(token):
        return jsonify({"error": "Token inválido"}), 401

    if accion == 'listar':
        lista = IngresosRepositorio.listar()
        return jsonify([i.serialize() for i in lista])
    elif accion == 'crear':
        id_usuario       = request.args.get('id_usuario')
        fecha_str        = request.args.get('fecha')
        fecha            = datetime.fromisoformat(fecha_str).date() if fecha_str else None
        monto            = request.args.get('monto')
        descripcion      = request.args.get('descripcion')
        id_moneda        = request.args.get('id_moneda')
        id_cuenta        = request.args.get('id_cuenta')
        id_metodo_pago   = request.args.get('id_metodo_pago')
        ing = Ingresos(id_usuario=id_usuario, fecha=fecha, monto=monto, descripcion=descripcion,
                     id_moneda=id_moneda, id_cuenta=id_cuenta, id_metodo_pago=id_metodo_pago)
        IngresosRepositorio.crear(ing)
        return jsonify({"mensaje": "Ingreso creado"})
    elif accion == 'actualizar':
        id_ingreso       = request.args.get('id_ingreso')
        id_usuario       = request.args.get('id_usuario')
        fecha_str        = request.args.get('fecha')
        fecha            = datetime.fromisoformat(fecha_str).date() if fecha_str else None
        monto            = request.args.get('monto')
        descripcion      = request.args.get('descripcion')
        id_moneda        = request.args.get('id_moneda')
        id_cuenta        = request.args.get('id_cuenta')
        id_metodo_pago   = request.args.get('id_metodo_pago')
        ing = Ingresos(id_ingreso=id_ingreso, id_usuario=id_usuario, fecha=fecha, monto=monto,
                     descripcion=descripcion, id_moneda=id_moneda, id_cuenta=id_cuenta,
                     id_metodo_pago=id_metodo_pago)
        IngresosRepositorio.actualizar(ing)
        return jsonify({"mensaje": "Ingreso actualizado"})
    elif accion == 'eliminar':
        id_ingreso = request.args.get('id_ingreso')
        IngresosRepositorio.eliminar(id_ingreso)
        return jsonify({"mensaje": "Ingreso eliminado"})
    else:
        return jsonify({"error": "Acción no válida"}), 400