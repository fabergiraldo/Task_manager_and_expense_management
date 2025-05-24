from flask import Flask, render_template
from Controlador.categorias_controller import categorias_controller
from Controlador.cuentas_bancarias_controller import cuentas_bancarias_controller
from Controlador.etiquetas_controller import etiquetas_controller
from Controlador.facturas_controller import facturas_controller
from Controlador.gastos_controller import gastos_controller
from Controlador.gastos_etiquetas_controller import gastos_etiquetas_controller
from Controlador.ingresos_controller import ingresos_controller
from Controlador.ingresos_etiquetas_controller import ingresos_etiquetas_controller
from Controlador.metodos_pago_controller import metodos_pago_controller
from Controlador.monedas_controller import monedas_controller
from Controlador.notificaciones_controller import notificaciones_controller
from Controlador.presupuestos_controller import presupuestos_controller
from Controlador.proveedores_controller import proveedores_controller
from Controlador.tarjetas_controller import tarjetas_controller
from Controlador.transacciones_controller import transacciones_controller
from Controlador.usuarios_controller import usuarios_controller

# importa otros controllers...

app = Flask(__name__)


app.register_blueprint(categorias_controller, url_prefix='/')
app.register_blueprint(cuentas_bancarias_controller, url_prefix='/')
app.register_blueprint(etiquetas_controller, url_prefix='/')
app.register_blueprint(facturas_controller, url_prefix='/')
app.register_blueprint(gastos_controller, url_prefix='/')
app.register_blueprint(gastos_etiquetas_controller, url_prefix='/')
app.register_blueprint(ingresos_controller, url_prefix='/')
app.register_blueprint(ingresos_etiquetas_controller, url_prefix='/')
app.register_blueprint(metodos_pago_controller, url_prefix='/')
app.register_blueprint(monedas_controller, url_prefix='/')
app.register_blueprint(notificaciones_controller, url_prefix='/')
app.register_blueprint(presupuestos_controller, url_prefix='/')
app.register_blueprint(proveedores_controller, url_prefix='/')
app.register_blueprint(tarjetas_controller, url_prefix='/')
app.register_blueprint(transacciones_controller, url_prefix='/')
app.register_blueprint(usuarios_controller, url_prefix='/')

# Ruta principal de documentación
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
