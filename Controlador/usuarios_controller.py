from flask import Blueprint, request, jsonify
import jwt
from Utilidades.Configuracion import SECRET_KEY, strConnection
from Repositorio.UsuariosRepositorio import UsuariosRepositorio
from Entidades.Usuarios import Usuarios
from datetime import datetime, timedelta

usuarios_controller = Blueprint('usuarios', __name__)

def verificar_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False

@usuarios_controller.route('/usuarios/token', methods=['GET'])
def obtener_token():
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    if usuario == "admin" and password == "password123":
        token = jwt.encode(
            {"usuario": usuario, "exp": datetime.utcnow() + timedelta(hours=1)},
            SECRET_KEY, algorithm="HS256"
        )
        return jsonify({"token": token})
    return jsonify({"error": "Credenciales inválidas"}), 401

@usuarios_controller.route('/usuarios/<accion>', methods=['GET'])
def usuarios_crud(accion):
    token = request.args.get('token')
    if not token or not verificar_token(token):
        return jsonify({"error": "Token inválido"}), 401

    # LISTAR
    if accion == "listar":
        lista = UsuariosRepositorio.listar()
        return jsonify([u.serialize() for u in lista])

    # CREAR
    elif accion == "crear":
        nombre    = request.args.get('nombre')
        correo    = request.args.get('correo')
        contrasena= request.args.get('contrasena')
        u = Usuarios(nombre=nombre, correo=correo, contrasena=contrasena)
        UsuariosRepositorio.crear(u)
        return jsonify({"mensaje": "Usuario creado"})

    # ACTUALIZAR
    elif accion == "actualizar":
        id_u      = request.args.get('id_usuario')
        nombre    = request.args.get('nombre')
        correo    = request.args.get('correo')
        contrasena= request.args.get('contrasena')
        u = Usuarios(id_usuario=id_u,
                    nombre=nombre,
                    correo=correo,
                    contrasena=contrasena)
        UsuariosRepositorio.actualizar(u)
        return jsonify({"mensaje": "Usuario actualizado"})

    # ELIMINAR
    elif accion == "eliminar":
        id_u = request.args.get('id_usuario')
        UsuariosRepositorio.eliminar(id_u)
        return jsonify({"mensaje": "Usuario eliminado"})

    else:
        return jsonify({"error": "Acción no válida"}), 400
