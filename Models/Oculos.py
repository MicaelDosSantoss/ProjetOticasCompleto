from uuid import uuid4
from Models.CRUD import CRUD

from flask import jsonify
import mysql.connector
from Database.database import conexao

class Oculos(CRUD):

    def __init__(self, Nome=None, ID_Oculos=None, ID_Material=None, ID_Forma=None, ID_Marca=None,
                 Cor=None, Tamanho=None, Genero=None, Valor=None, Data_Recebimento=None, Imagem=None):
        self.ID_Oculos = ID_Oculos if ID_Oculos else str(uuid4())
        self.ID_Material = ID_Material
        self.ID_Forma = ID_Forma
        self.ID_Marca = ID_Marca
        self.Nome = Nome
        self.Cor = Cor
        self.Tamanho = Tamanho
        self.Genero = Genero
        self.Valor = Valor
        self.Data_Recebimento = Data_Recebimento
        self.Imagem = Imagem  # novo campo para nome do arquivo da imagem

    def salvar(self):
        try:

            if self.ID_Material is None:
                print("ID_Material não fornecido.")
                return

            if self.ID_Forma is None:
                print("ID_Forma não fornecido.")
                return

            if self.ID_Marca is None:
                print("ID_Marca não fornecido.")
                return

            if self.Nome is None:
                print("Nome não fornecido.")
                return

            if self.Cor is None:
                print("Cor não fornecido.")
                return

            if self.Tamanho is None:
                print("Tamanho não fornecido.")
                return

            if self.Genero is None:
                print("Genero não fornecido.")
                return

            if self.Valor is None:
                print("Valor não fornecido.")
                return

            if self.Data_Recebimento is None:
                print("Data_Recebimento não fornecido.")
                return

            conn = conexao()
            if conn is None:
                print("Falha na conexão.")
                return

            cursor = conn.cursor()

            if self.Imagem:
                query = """
                    INSERT INTO oculos (
                        ID_Oculos,
                        ID_Material,
                        ID_Forma,
                        ID_Marca,
                        Nome,
                        Cor,
                        Tamanho,
                        Genero,
                        Valor,
                        Data_Recebimento,
                        Imagem
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                valores = (
                    self.ID_Oculos,
                    self.ID_Material,
                    self.ID_Forma,
                    self.ID_Marca,
                    self.Nome,
                    self.Cor,
                    self.Tamanho,
                    self.Genero,
                    self.Valor,
                    self.Data_Recebimento,
                    self.Imagem
                )
            else:
                query = """
                    INSERT INTO oculos (
                        ID_Oculos,
                        ID_Material,
                        ID_Forma,
                        ID_Marca,
                        Nome,
                        Cor,
                        Tamanho,
                        Genero,
                        Valor,
                        Data_Recebimento
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                valores = (
                    self.ID_Oculos,
                    self.ID_Material,
                    self.ID_Forma,
                    self.ID_Marca,
                    self.Nome,
                    self.Cor,
                    self.Tamanho,
                    self.Genero,
                    self.Valor,
                    self.Data_Recebimento
                )

            cursor.execute(query, valores)
            conn.commit()
            cursor.close()
            conn.close()
            print("Registro inserido com sucesso.")

        except mysql.connector.Error as err:
            print(f"Erro ao registrar: {err}")

    @staticmethod
    def mostrarTudo():
        try:
            conn = conexao()
            if conn is None:
                return jsonify({'erro': 'Falha na conexão com o banco'}), 500

            cursor = conn.cursor()
            query = "SELECT * FROM oculos"
            cursor.execute(query)
            resultados = cursor.fetchall()

            lista = []
            for row in resultados:
                lista.append({
                    "ID_Oculos": row[0],
                    "Nome": row[1],
                    "ID_Material": row[2],
                    "Cor": row[3],
                    "Tamanho": row[4],
                    "ID_Marca": row[5],
                    "Genero": row[6],
                    "ID_Forma": row[7],
                    "Valor": float(row[8]) if row[8] else None,
                    "Data_Recebimento": str(row[9]) if row[9] else None,
                    "Imagem": row[10] if len(row) > 10 else None
                })

            cursor.close()
            conn.close()

            if not lista:
                return jsonify({"mensagem": "Nenhum óculos encontrado."}), 404

            return lista

        except mysql.connector.Error as err:
            return jsonify({'erro': f'Erro ao buscar óculos: {err}'}), 500

    @staticmethod
    def buscarPorId(id):
        try:
            conn = conexao()
            if conn is None:
                return jsonify({'erro': 'Falha na conexão com o banco'}), 500

            cursor = conn.cursor()
            query = "SELECT * FROM oculos WHERE ID_Oculos = %s"
            cursor.execute(query, (id.strip(),))
            row = cursor.fetchone()

            cursor.close()
            conn.close()

            if not row:
                return jsonify({'mensagem': 'Óculos não encontrado!'}), 404

            resultado = {
                "ID_Oculos": row[0],
                "Nome": row[1],
                "ID_Material": row[2],
                "Cor": row[3],
                "Tamanho": row[4],
                "ID_Marca": row[5],
                "Genero": row[6],
                "ID_Forma": row[7],
                "Valor": float(row[8]) if row[8] else None,
                "Data_Recebimento": str(row[9]) if row[9] else None,
                "Imagem": row[10] if len(row) > 10 else None
            }

            return jsonify(resultado), 200

        except mysql.connector.Error as err:
            return jsonify({'erro': f'Erro ao buscar óculos por ID: {err}'}), 500

    @staticmethod
    def atualizar(id, body_response):
        try:
            conn = conexao()
            if conn is None:
                return jsonify({'erro': 'Falha na conexão com o banco'}), 500

            cursor = conn.cursor(dictionary=True)

            # Buscar os dados atuais
            cursor.execute("SELECT * FROM oculos WHERE ID_Oculos = %s", (id,))
            atual = cursor.fetchone()

            if not atual:
                return jsonify({'mensagem': 'Óculos não encontrado!'}), 404

            # Substituir apenas os campos enviados
            campos = [
                "ID_Material", "ID_Forma", "ID_Marca", "Nome", "Cor",
                "Tamanho", "Genero", "Valor", "Data_Recebimento", "Imagem"
            ]
            novos_valores = [body_response.get(campo, atual[campo]) for campo in campos]

            query = """
                UPDATE oculos SET
                    ID_Material = %s,
                    ID_Forma = %s,
                    ID_Marca = %s,
                    Nome = %s,
                    Cor = %s,
                    Tamanho = %s,
                    Genero = %s,
                    Valor = %s,
                    Data_Recebimento = %s,
                    Imagem = %s
                WHERE ID_Oculos = %s
            """

            cursor.execute(query, (*novos_valores, id))
            conn.commit()
            cursor.close()
            conn.close()

            return jsonify({'mensagem': 'Óculos atualizado com sucesso!'}), 200

        except mysql.connector.Error as err:
            return jsonify({'erro': f'Erro ao atualizar óculos: {err}'}), 500

    @staticmethod
    def deletar(id):
        return CRUD.deletar("oculos", "ID_Oculos", id)
