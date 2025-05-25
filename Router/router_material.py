
from flask import Flask, render_template, jsonify, request, Blueprint, redirect

from Models.Material import Material

material_bp = Blueprint('material', __name__)

@material_bp.route('/material', methods=['POST'])
def registarMaterial():
    nome_material = request.form.get('Nome') or (request.json.get('Nome') if request.is_json else None)

    if not nome_material:
        return jsonify({'error': 'Nome da marca não fornecido'}), 400

    material = Material(Nome=nome_material)
    material.salvar()

    return redirect('/material')

@material_bp.route('/material', methods=['GET'])
def mostrarMaterial():
    material = Material.mostrar("material","ID_Material")

    if not material:
        # Você pode criar uma página de erro, ou passar uma mensagem para o template
        return render_template('marca.html', materiais=None, error="Nenhuma marca encontrada!")

    return render_template('controller_material.html', materiais=material)

@material_bp.route('/material/<id>', methods=['GET'])
def get_material(id):
    return Material.buscarPorId(id)

@material_bp.route('/material/edit/<id>', methods=['PUT'])
def update_material(id):
    if not request.json or 'Nome' not in request.json:
        return jsonify({'error': 'Nome da forma não fornecido'}), 400

    nome_material = request.json['Nome']
    return Material.atualizar(id, nome_material)

@material_bp.route('/material/delete/<id>', methods=['DELETE'])
def delete_material(id):
    return Material.deletar(id)