from flask import Blueprint, request, jsonify, render_template, redirect
from Models.Oculos import Oculos

from Models.Forma import Forma
from Models.Material import Material
from Models.Marca import Marca
from werkzeug.utils import secure_filename
import os

oculos_bp = Blueprint('oculos', __name__)

UPLOAD_FOLDER = 'static/uploads'

@oculos_bp.route('/oculos', methods=['POST'])
def criar_oculos():
    form = request.form
    imagem = request.files.get('Imagem')

    oculos = Oculos(
        Nome=form.get('Nome'),
        ID_Material=form.get('ID_Material'),
        ID_Forma=form.get('ID_Forma'),
        ID_Marca=form.get('ID_Marca'),
        Cor=form.get('Cor'),
        Tamanho=form.get('Tamanho'),
        Genero=form.get('Genero'),
        Valor=form.get('Valor'),
        Data_Recebimento=form.get('Data_Recebimento')
    )

    if imagem and imagem.filename != '':
        filename = secure_filename(imagem.filename)
        caminho = os.path.join(UPLOAD_FOLDER, filename)
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        imagem.save(caminho)
        oculos.Imagem = filename

    oculos.salvar()
    return redirect('/oculos')

@oculos_bp.route('/oculos/update/<id>', methods=['PUT'])
def atualizar_oculos(id):
    if request.content_type.startswith('multipart/form-data'):
        form = request.form.to_dict()
        imagem = request.files.get('Imagem')
    else:
        form = request.get_json() or {}
        imagem = None

    if imagem and imagem.filename != '':
        filename = secure_filename(imagem.filename)
        caminho = os.path.join(UPLOAD_FOLDER, filename)
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        imagem.save(caminho)
        form['Imagem'] = filename

    resp = Oculos.atualizar(id, form)
    return resp

@oculos_bp.route('/oculos', methods=['GET'])
def mostrar_todos_oculos():
    oculo = Oculos.mostrarTudo()

    marca = Marca.mostrar("marca", "ID_Marca")
    forma = Forma.mostrar("forma", "ID_Forma")
    material = Material.mostrar("material", "ID_Material")

    if not oculo:
        return jsonify({"Message": "Oculos não encontrado!"})

    return render_template('controller_oculos.html',oculos=oculo, marcas=marca, formas=forma, materiais=material)

@oculos_bp.route('/home', methods=['GET'])
def home():
    oculo = Oculos.mostrarTudo()

    if not oculo:
        return jsonify({"Message": "Oculos não encontrado!"})

    return render_template('home.html',oculos=oculo)

@oculos_bp.route('/oculos/<id>', methods=['GET'])
def buscar_oculos_por_id(id):
        resposta = Oculos.buscarPorId(id)
        # `resposta` aqui é um tuple: (jsonify, status)
        # Então vamos pegar o JSON para passar para o template

        if resposta[1] != 200:
            return f"Erro: {resposta[0].json['mensagem'] if 'mensagem' in resposta[0].json else 'Não encontrado'}"

        dados = resposta[0].json  # Aqui está o dict com as chaves

        return render_template('oculos_id.html', oculos_id=dados)

@oculos_bp.route('/oculos/delete/<id>', methods=['DELETE'])
def deletar_oculos(id):
    return Oculos.deletar(id)
