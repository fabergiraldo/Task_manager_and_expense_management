from flask import Blueprint, request, jsonify
import jwt
from Utilidades.Configuracion import SECRET_KEY
from Repositorio.IngresosEtiquetasRepositorio import IngresosEtiquetasRepositorio
from Entidades.IngresosEtiquetas import IngresosEtiquetas
from datetime import datetime, timedelta

ingresos_etiquetas_controller = Blueprint('ingresos_etiquetas', __name__)

def verificar_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False

@ingresos_etiquetas_controller.route('/ingresos_etiquetas/token', methods=['GET'])
def obtener_token_ingresos_etiquetas():
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    if usuario == "admin" and password == "password123":
        token = jwt.encode(
            {"usuario": usuario, "exp": datetime.utcnow() + timedelta(hours=1)},
            SECRET_KEY, algorithm="HS256"
        )
        return jsonify({"token": token})
    return jsonify({"error": "Credenciales inválidas"}), 401

@ingresos_etiquetas_controller.route('/ingresos_etiquetas/<accion>', methods=['GET'])
def ingresos_etiquetas_crud(accion):
    token = request.args.get('token')
    if not token or not verificar_token(token):
        return jsonify({"error": "Token inválido"}), 401

    if accion == 'listar':
        lista = IngresosEtiquetasRepositorio.listar()
        return jsonify([r.serialize() for r in lista])
    elif accion == 'crear':
        id_ingreso = request.args.get('id_ingreso')
        id_etiqueta = request.args.get('id_etiqueta')
        relacion = IngresosEtiquetas(id_ingreso=id_ingreso, id_etiqueta=id_etiqueta)
        IngresosEtiquetasRepositorio.crear(relacion)
        return jsonify({"mensaje": "Relación ingreso-etiqueta creada"})
    elif accion == 'eliminar':
        id_ingreso = request.args.get('id_ingreso')
        id_etiqueta = request.args.get('id_etiqueta')
        IngresosEtiquetasRepositorio.eliminar(id_ingreso, id_etiqueta)
        return jsonify({"mensaje": "Relación ingreso-etiqueta eliminada"})
    else:
        return jsonify({"error": "Acción no válida"}), 400
