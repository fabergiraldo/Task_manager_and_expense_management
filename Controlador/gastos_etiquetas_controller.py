from flask import Blueprint, request, jsonify
import jwt
from Utilidades.Configuracion import SECRET_KEY
from Repositorio.GastosEtiquetasRepositorio import GastosEtiquetasRepositorio
from Entidades.GastosEtiquetas import GastosEtiquetas
from datetime import datetime, timedelta


gastos_etiquetas_controller = Blueprint('gastos_etiquetas', __name__)

def verificar_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except jwt.InvalidTokenError:
        return False

@gastos_etiquetas_controller.route('/gastos_etiquetas/token', methods=['GET'])
def obtener_token_gastos_etiquetas():
    usuario = request.args.get('usuario')
    password = request.args.get('password')
    if usuario == "admin" and password == "password123":
        token = jwt.encode(
            {"usuario": usuario, "exp": datetime.utcnow() + timedelta(hours=1)},
            SECRET_KEY, algorithm="HS256"
        )
        return jsonify({"token": token})
    return jsonify({"error": "Credenciales inválidas"}), 401

@gastos_etiquetas_controller.route('/gastos_etiquetas/<accion>', methods=['GET'])
def gastos_etiquetas_crud(accion):
    token = request.args.get('token')
    if not token or not verificar_token(token):
        return jsonify({"error": "Token inválido"}), 401

    if accion == 'listar':
        lista = GastosEtiquetasRepositorio.listar()
        return jsonify([r.serialize() for r in lista])
    elif accion == 'crear':
        id_gasto = request.args.get('id_gasto')
        id_etiqueta = request.args.get('id_etiqueta')
        relacion = GastosEtiquetas(id_gasto=id_gasto, id_etiqueta=id_etiqueta)
        GastosEtiquetasRepositorio.crear(relacion)
        return jsonify({"mensaje": "Relación gasto-etiqueta creada"})
    elif accion == 'eliminar':
        id_gasto = request.args.get('id_gasto')
        id_etiqueta = request.args.get('id_etiqueta')
        GastosEtiquetasRepositorio.eliminar(id_gasto, id_etiqueta)
        return jsonify({"mensaje": "Relación gasto-etiqueta eliminada"})
    else:
        return jsonify({"error": "Acción no válida"}), 400
