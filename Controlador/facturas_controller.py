from flask import Blueprint, request, jsonify
import jwt
from Utilidades.Configuracion import SECRET_KEY
from Repositorio.FacturasRepositorio import FacturasRepositorio
from Entidades.Facturas import Facturas
from datetime import datetime, timedelta

facturas_controller = Blueprint('facturas', __name__)

def verificar_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False

@facturas_controller.route('/facturas/token', methods=['GET'])
def obtener_token_facturas():
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    if usuario == "admin" and password == "password123":
        token = jwt.encode({"usuario": usuario, "exp": datetime.utcnow() + timedelta(hours=1)}, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token})
    return jsonify({"error": "Credenciales inválidas"}), 401

@facturas_controller.route('/facturas/<accion>', methods=['GET'])
def facturas_crud(accion):
    token = request.args.get('token')
    if not token or not verificar_token(token):
        return jsonify({"error": "Token inválido"}), 401

    if accion == 'listar':
        lista = FacturasRepositorio.listar()
        return jsonify([f.serialize() for f in lista])
    elif accion == 'crear':
        id_gasto = request.args.get('id_gasto')
        id_proveedor = request.args.get('id_proveedor')
        ruta_archivo = request.args.get('ruta_archivo')
        f = Facturas(id_gasto=id_gasto, id_proveedor=id_proveedor, ruta_archivo=ruta_archivo)
        FacturasRepositorio.crear(f)
        return jsonify({"mensaje": "Factura creada"})
    elif accion == 'actualizar':
        id_factura = request.args.get('id_factura')
        id_gasto = request.args.get('id_gasto')
        id_proveedor = request.args.get('id_proveedor')
        ruta_archivo = request.args.get('ruta_archivo')
        f = Facturas(id_factura=id_factura, id_gasto=id_gasto, id_proveedor=id_proveedor, ruta_archivo=ruta_archivo)
        FacturasRepositorio.actualizar(f)
        return jsonify({"mensaje": "Factura actualizada"})
    elif accion == 'eliminar':
        id_factura = request.args.get('id_factura')
        FacturasRepositorio.eliminar(id_factura)
        return jsonify({"mensaje": "Factura eliminada"})
    else:
        return jsonify({"error": "Acción no válida"}), 400
