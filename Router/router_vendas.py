from flask import Blueprint, request, jsonify, render_template
from Models.Vendas import Venda
from Models.Oculos import Oculos

venda_bp = Blueprint('venda', __name__)

@venda_bp.route('/vendas', methods=['POST'])
def criar_venda():
    form = request.form

    venda = Venda(
        ID_Oculos=form.get('ID_Oculos'),
        Nome_Cartao=form.get('Nome_Cartao'),
        Numero_Cartao=form.get('Numero_Cartao'),
        CEP=form.get('CEP'),
        Endereco=form.get('Endereco'),
        Cidade=form.get('Cidade'),
        Estado=form.get('Estado'),
        Complemento=form.get('Complemento')
    )

    return venda.salvar()

@venda_bp.route('/<id>/pag', methods=['GET'])
def pagamento_view(id):
    oculos = Oculos.buscarPorId(id)
    if not oculos:
        return "Óculos não encontrado", 404
    return render_template("pagamento.html", oculos_id=oculos)