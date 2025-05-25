from flask import Flask
from Router.router_marcas import marca_bp
from Router.router_formas import forma_bp
from Router.router_material import material_bp
from Router.router_oculos import oculos_bp
from Router.router_vendas import venda_bp

app = Flask(__name__)
app.register_blueprint(marca_bp)
app.register_blueprint(forma_bp)
app.register_blueprint(material_bp)
app.register_blueprint(oculos_bp)
app.register_blueprint(venda_bp)

if __name__ == '__main__':
    app.run(debug=True)