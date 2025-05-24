from flask import Blueprint, request, jsonify
import jwt
from Utilidades.Configuracion import SECRET_KEY
from Repositorio.PresupuestosRepositorio import PresupuestosRepositorio
from Entidades.Presupuestos import Presupuestos
from datetime import datetime, timedelta

presupuestos_controller = Blueprint('presupuestos', __name__)

def verificar_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False

@presupuestos_controller.route('/presupuestos/token', methods=['GET'])
def obtener_token_presupuestos():
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    if usuario == "admin" and password == "password123":
        token = jwt.encode({"usuario": usuario, "exp": datetime.utcnow() + timedelta(hours=1)}, SECRET_KEY, algorithm="HS256")
        return jsonify({"token": token})
    return jsonify({"error": "Credenciales inválidas"}), 401

@presupuestos_controller.route('/presupuestos/<accion>', methods=['GET'])
def presupuestos_crud(accion):
    token = request.args.get('token')
    if not token or not verificar_token(token):
        return jsonify({"error": "Token inválido"}), 401

    if accion == 'listar':
        lista = PresupuestosRepositorio.listar()
        return jsonify([p.serialize() for p in lista])
    elif accion == 'crear':
        id_usuario = request.args.get('id_usuario')
        id_categoria = request.args.get('id_categoria')
        mes = request.args.get('mes')  # '2025'
        monto = request.args.get('monto')
        p = Presupuestos(id_usuario=id_usuario, id_categoria=id_categoria, mes=mes, monto=monto)
        PresupuestosRepositorio.crear(p)
        return jsonify({"mensaje": "Presupuesto creado"})
    elif accion == 'actualizar':
        id_presupuesto = request.args.get('id_presupuesto')
        id_usuario = request.args.get('id_usuario')
        id_categoria = request.args.get('id_categoria')
        mes = request.args.get('mes')
        monto = request.args.get('monto')
        p = Presupuestos(id_presupuesto=id_presupuesto, id_usuario=id_usuario,
                         id_categoria=id_categoria, mes=mes, monto=monto)
        PresupuestosRepositorio.actualizar(p)
        return jsonify({"mensaje": "Presupuesto actualizado"})
    elif accion == 'eliminar':
        id_presupuesto = request.args.get('id_presupuesto')
        PresupuestosRepositorio.eliminar(id_presupuesto)
        return jsonify({"mensaje": "Presupuesto eliminado"})
    else:
        return jsonify({"error": "Acción no válida"}), 400
