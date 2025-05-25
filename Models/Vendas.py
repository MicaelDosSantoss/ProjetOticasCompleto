from uuid import uuid4
from flask import jsonify
import mysql.connector
from Database.database import conexao

class Venda:
    def __init__(self, ID_Oculos, Nome_Cartao, Numero_Cartao,
                 CEP, Endereco, Cidade, Estado, Complemento):
        self.ID_Venda = str(uuid4())
        self.ID_Oculos = ID_Oculos
        self.Nome_Cartao = Nome_Cartao
        self.Numero_Cartao = Numero_Cartao
        self.CEP = CEP
        self.Endereco = Endereco
        self.Cidade = Cidade
        self.Estado = Estado
        self.Complemento = Complemento

    def salvar(self):
        try:
            conn = conexao()
            if conn is None:
                return jsonify({"erro": "Falha na conexão com o banco"}), 500

            cursor = conn.cursor()
            query = """
                INSERT INTO vendas (
                    ID_Venda,
                    ID_Oculos,
                    Nome_Cartao,
                    Numero_Cartao,
                    CEP,
                    Endereco,
                    Cidade,
                    Estado,
                    Complemento
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                self.ID_Venda,
                self.ID_Oculos,
                self.Nome_Cartao,
                self.Numero_Cartao,
                self.CEP,
                self.Endereco,
                self.Cidade,
                self.Estado,
                self.Complemento
            )

            cursor.execute(query, valores)
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"mensagem": "Venda registrada com sucesso!", "ID_Venda": self.ID_Venda}), 201

        except mysql.connector.Error as err:
            return jsonify({'erro': f'Erro ao registrar venda: {err}'}), 500

    @staticmethod
    def mostrarTudo():
        try:
            conn = conexao()
            if conn is None:
                return jsonify({"erro": "Falha na conexão com o banco"}), 500

            cursor = conn.cursor()
            query = "SELECT * FROM vendas"
            cursor.execute(query)
            resultados = cursor.fetchall()

            vendas = []
            for row in resultados:
                vendas.append({
                    "ID_Venda": row[0],
                    "ID_Oculos": row[1],
                    "Nome_Cartao": row[2],
                    "Numero_Cartao": row[3],
                    "CEP": row[4],
                    "Endereco": row[5],
                    "Cidade": row[6],
                    "Estado": row[7],
                    "Complemento": row[8],
                    "Data_Venda": str(row[9])
                })

            cursor.close()
            conn.close()

            return redirect("/home")

        except mysql.connector.Error as err:
            return jsonify({"erro": f"Erro ao buscar vendas: {err}"}), 500