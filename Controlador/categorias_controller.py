from flask import Blueprint, request, jsonify
import jwt
from Utilidades.Configuracion import SECRET_KEY
from Repositorio.CategoriasRepositorio import CategoriasRepositorio
from Entidades.Categorias import Categorias
from datetime import datetime, timedelta

categorias_controller = Blueprint('categorias', __name__)

def verificar_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False

@categorias_controller.route('/categorias/token', methods=['GET'])
def obtener_token_categorias():
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    if usuario == "admin" and password == "password123":
        token = jwt.encode(
            {"usuario": usuario, "exp": datetime.utcnow() + timedelta(hours=1)},
            SECRET_KEY, algorithm="HS256"
        )
        return jsonify({"token": token})
    return jsonify({"error": "Credenciales inválidas"}), 401

@categorias_controller.route('/categorias/<accion>', methods=['GET'])
def categorias_crud(accion):
    token = request.args.get('token')
    if not token or not verificar_token(token):
        return jsonify({"error": "Token inválido"}), 401

    if accion == 'listar':
        lista = CategoriasRepositorio.listar()
        return jsonify([c.serialize() for c in lista])
    elif accion == 'crear':
        nombre = request.args.get('nombre')
        descripcion = request.args.get('descripcion')
        c = Categorias(nombre=nombre, descripcion=descripcion)
        CategoriasRepositorio.crear(c)
        return jsonify({"mensaje": "Categoría creada"})
    elif accion == 'actualizar':
        id_cat = request.args.get('id_categoria')
        nombre = request.args.get('nombre')
        descripcion = request.args.get('descripcion')
        c = Categorias(id_categoria=id_cat, nombre=nombre, descripcion=descripcion)
        CategoriasRepositorio.actualizar(c)
        return jsonify({"mensaje": "Categoría actualizada"})
    elif accion == 'eliminar':
        id_cat = request.args.get('id_categoria')
        CategoriasRepositorio.eliminar(id_cat)
        return jsonify({"mensaje": "Categoría eliminada"})
    else:
        return jsonify({"error": "Acción no válida"}), 400