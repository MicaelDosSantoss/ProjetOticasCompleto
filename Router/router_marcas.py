
from flask import Flask, render_template, jsonify, request, Blueprint, redirect
from flask import render_template

from Models.Marca import Marca

marca_bp = Blueprint('marca', __name__)

@marca_bp.route('/marca', methods=['POST'])
def registarMarca():
    nome_marca = request.form.get('Nome') or (request.json.get('Nome') if request.is_json else None)

    if not nome_marca:
        return jsonify({'error': 'Nome da marca não fornecido'}), 400

    marca = Marca(Nome=nome_marca)
    marca.salvar()

    return redirect('/marca')


@marca_bp.route('/marca', methods=['GET'])
def mostrarMarca():
    marca = Marca.mostrar("marca", "ID_Marca")

    if not marca:
        # Você pode criar uma página de erro, ou passar uma mensagem para o template
        return render_template('marca.html', marcas=None, error="Nenhuma marca encontrada!")

    return render_template('controller_marca.html', marcas=marca)

@marca_bp.route('/marca/<id>', methods=['GET'])
def get_marca(id):
    return Marca.buscarPorId(id)

@marca_bp.route('/marca/edit/<id>', methods=['PUT'])
def update_marca(id):
    if not request.json or 'Nome' not in request.json:
        return jsonify({'error': 'Nome da marca não fornecido'}), 400

    nome_marca = request.json['Nome']
    return Marca.atualizar(id, nome_marca)

@marca_bp.route('/marca/delete/<id>', methods=['DELETE'])
def delete_marca(id):
    return Marca.deletar(id)