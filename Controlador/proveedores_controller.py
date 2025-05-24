from flask import Blueprint, request, jsonify
import jwt
from Utilidades.Configuracion import SECRET_KEY
from Repositorio.ProveedoresRepositorio import ProveedoresRepositorio
from Entidades.Proveedores import Proveedores
from datetime import datetime, timedelta

proveedores_controller = Blueprint('proveedores', __name__)

def verificar_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False

@proveedores_controller.route('/proveedores/token', methods=['GET'])
def obtener_token_proveedores():
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    if usuario == "admin" and password == "password123":
        token = jwt.encode({"usuario": usuario, "exp": datetime.utcnow() + timedelta(hours=1)}, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token})
    return jsonify({"error": "Credenciales inválidas"}), 401

@proveedores_controller.route('/proveedores/<accion>', methods=['GET'])
def proveedores_crud(accion):
    token = request.args.get('token')
    if not token or not verificar_token(token):
        return jsonify({"error": "Token inválido"}), 401

    if accion == 'listar':
        lista = ProveedoresRepositorio.listar()
        return jsonify([p.serialize() for p in lista])
    elif accion == 'crear':
        nombre   = request.args.get('nombre')
        contacto = request.args.get('contacto')
        telefono = request.args.get('telefono')
        correo   = request.args.get('correo')
        p = Proveedores(nombre=nombre, contacto=contacto, telefono=telefono, correo=correo)
        ProveedoresRepositorio.crear(p)
        return jsonify({"mensaje": "Proveedor creado"})
    elif accion == 'actualizar':
        id_pr    = request.args.get('id_proveedor')
        nombre   = request.args.get('nombre')
        contacto = request.args.get('contacto')
        telefono = request.args.get('telefono')
        correo   = request.args.get('correo')
        p = Proveedores(id_proveedor=id_pr, nombre=nombre, contacto=contacto, telefono=telefono, correo=correo)
        ProveedoresRepositorio.actualizar(p)
        return jsonify({"mensaje": "Proveedor actualizado"})
    elif accion == 'eliminar':
        id_pr = request.args.get('id_proveedor')
        ProveedoresRepositorio.eliminar(id_pr)
        return jsonify({"mensaje": "Proveedor eliminado"})
    else:
        return jsonify({"error": "Acción no válida"}), 400
