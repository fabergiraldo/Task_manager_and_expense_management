from flask import Blueprint, request, jsonify
import jwt
from Utilidades.Configuracion import SECRET_KEY
from Repositorio.GastosRepositorio import GastosRepositorio
from Entidades.Gastos import Gastos
from datetime import datetime, timedelta


gastos_controller = Blueprint('gastos', __name__)

# Reutilizar verificar_token si importable o reimplementar:

def verificar_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False

@gastos_controller.route('/gastos/token', methods=['GET'])
def obtener_token_gastos():
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    if usuario == "admin" and password == "password123":
        token = jwt.encode({"usuario": usuario, "exp": datetime.utcnow() + timedelta(hours=1)}, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token})
    return jsonify({"error": "Credenciales inválidas"}), 401

@gastos_controller.route('/gastos/<accion>', methods=['GET'])
def gastos_crud(accion):
    token = request.args.get('token')
    if not token or not verificar_token(token):
        return jsonify({"error": "Token inválido"}), 401

    if accion == 'listar':
        lista = GastosRepositorio.listar()
        return jsonify([g.serialize() for g in lista])

    # CREAR
    elif accion == 'crear':
        id_usuario     = request.args.get('id_usuario')
        fecha_str      = request.args.get('fecha')
        fecha          = datetime.fromisoformat(fecha_str).date() if fecha_str else None
        monto          = request.args.get('monto')
        descripcion    = request.args.get('descripcion')
        id_categoria   = request.args.get('id_categoria')
        id_moneda      = request.args.get('id_moneda')
        id_cuenta      = request.args.get('id_cuenta')
        id_tarjeta     = request.args.get('id_tarjeta')
        id_proveedor   = request.args.get('id_proveedor')
        id_metodo_pago = request.args.get('id_metodo_pago')
        g = Gastos(id_usuario=id_usuario, fecha=fecha, monto=monto, descripcion=descripcion,
                 id_categoria=id_categoria, id_moneda=id_moneda, id_cuenta=id_cuenta,
                 id_tarjeta=id_tarjeta, id_proveedor=id_proveedor, id_metodo_pago=id_metodo_pago)
        GastosRepositorio.crear(g)
        return jsonify({"mensaje": "Gasto creado"})

    # ACTUALIZAR
    elif accion == 'actualizar':
        id_gasto       = request.args.get('id_gasto')
        id_usuario     = request.args.get('id_usuario')
        fecha_str      = request.args.get('fecha')
        fecha          = datetime.fromisoformat(fecha_str).date() if fecha_str else None
        monto          = request.args.get('monto')
        descripcion    = request.args.get('descripcion')
        id_categoria   = request.args.get('id_categoria')
        id_moneda      = request.args.get('id_moneda')
        id_cuenta      = request.args.get('id_cuenta')
        id_tarjeta     = request.args.get('id_tarjeta')
        id_proveedor   = request.args.get('id_proveedor')
        id_metodo_pago = request.args.get('id_metodo_pago')
        g = Gastos(id_gasto=id_gasto, id_usuario=id_usuario, fecha=fecha, monto=monto, descripcion=descripcion,
                 id_categoria=id_categoria, id_moneda=id_moneda, id_cuenta=id_cuenta,
                 id_tarjeta=id_tarjeta, id_proveedor=id_proveedor, id_metodo_pago=id_metodo_pago)
        GastosRepositorio.actualizar(g)
        return jsonify({"mensaje": "Gasto actualizado"})

    # ELIMINAR
    elif accion == 'eliminar':
        id_gasto = request.args.get('id_gasto')
        GastosRepositorio.eliminar(id_gasto)
        return jsonify({"mensaje": "Gasto eliminado"})

    else:
        return jsonify({"error": "Acción no válida"}), 400