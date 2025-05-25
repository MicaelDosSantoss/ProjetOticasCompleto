
from flask import Flask, render_template, jsonify, request, Blueprint, redirect

from Models.Forma import Forma

forma_bp = Blueprint('forma', __name__)

@forma_bp.route('/forma', methods=['POST'])
def registarFormas():
    nome_forma = request.form.get('Nome') or (request.json.get('Nome') if request.is_json else None)

    if not nome_forma:
        return jsonify({'error': 'Nome da marca não fornecido'}), 400

    forma = Forma(Nome=nome_forma)
    forma.salvar()

    return redirect('/forma')

@forma_bp.route('/forma', methods=['GET'])
def mostrarFormas():
    forma = Forma.mostrar("forma","ID_Forma")

    if not forma:
        # Você pode criar uma página de erro, ou passar uma mensagem para o template
        return render_template('marca.html', formas=None, error="Nenhuma marca encontrada!")

    return render_template('controller_forma.html', formas=forma)

@forma_bp.route('/forma/<id>', methods=['GET'])
def get_forma(id):
    return Forma.buscarPorId(id)

@forma_bp.route('/forma', methods=['POST'])
def registarForma():
    if not request.json or 'Nome' not in request.json:
        return jsonify({'error': 'Nome da forma não fornecido'}), 400

    nome_forma = request.json['Nome']

    forma = Forma( Nome = nome_forma )
    forma.salvar()

    return redirect("/forma")

@forma_bp.route('/forma/edit/<id>', methods=['PUT'])
def update_forma(id):
    if not request.json or 'Nome' not in request.json:
        return jsonify({'error': 'Nome da forma não fornecido'}), 400

    nome_forma = request.json['Nome']
    return Forma.atualizar(id, nome_forma)

@forma_bp.route('/forma/delete/<id>', methods=['DELETE'])
def delete_forma(id):
    return Forma.deletar(id)

