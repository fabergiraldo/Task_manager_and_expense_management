from flask import Blueprint, request, jsonify
import jwt
from Utilidades.Configuracion import SECRET_KEY
from Repositorio.NotificacionesRepositorio import NotificacionesRepositorio
from Entidades.Notificaciones import Notificaciones
from datetime import datetime, timedelta

notificaciones_controller = Blueprint('notificaciones', __name__)

def verificar_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False

@notificaciones_controller.route('/notificaciones/token', methods=['GET'])
def obtener_token_notificaciones():
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    if usuario == "admin" and password == "password123":
        token = jwt.encode({"usuario": usuario, "exp": datetime.utcnow() + timedelta(hours=1)}, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token})
    return jsonify({"error": "Credenciales inválidas"}), 401

@notificaciones_controller.route('/notificaciones/<accion>', methods=['GET'])
def notificaciones_crud(accion):
    token = request.args.get('token')
    if not token or not verificar_token(token):
        return jsonify({"error": "Token inválido"}), 401

    if accion == 'listar':
        lst = NotificacionesRepositorio.listar()
        return jsonify([n.serialize() for n in lst])
    elif accion == 'crear':
        id_usuario = request.args.get('id_usuario')
        mensaje = request.args.get('mensaje')
        fecha_str = request.args.get('fecha')
        fecha = datetime.fromisoformat(fecha_str) if fecha_str else datetime.utcnow()
        leido = request.args.get('leido', 'false').lower() == 'true'
        n = Notificaciones(id_usuario=id_usuario, mensaje=mensaje, fecha=fecha, leido=leido)
        NotificacionesRepositorio.crear(n)
        return jsonify({"mensaje": "Notificación creada"})
    elif accion == 'actualizar':
        id_not = request.args.get('id_notificacion')
        id_usuario = request.args.get('id_usuario')
        mensaje = request.args.get('mensaje')
        fecha_str = request.args.get('fecha')
        fecha = datetime.fromisoformat(fecha_str) if fecha_str else datetime.utcnow()
        leido = request.args.get('leido', 'false').lower() == 'true'
        n = Notificaciones(id_notificacion=id_not, id_usuario=id_usuario, mensaje=mensaje, fecha=fecha, leido=leido)
        NotificacionesRepositorio.actualizar(n)
        return jsonify({"mensaje": "Notificación actualizada"})
    elif accion == 'eliminar':
        id_not = request.args.get('id_notificacion')
        NotificacionesRepositorio.eliminar(id_not)
        return jsonify({"mensaje": "Notificación eliminada"})
    else:
        return jsonify({"error": "Acción no válida"}), 400
