from uuid import uuid4
from Models.CRUD import CRUD

class Forma(CRUD):
    def __init__(self, Nome=None, ID_Forma=None):
        self.ID_Forma = ID_Forma if ID_Forma else str(uuid4())
        self.Nome = Nome

    def salvar(self):
        self.registar("forma","ID_Forma")

    def mostrarTudo(self):
        self.mostrar("forma","ID_Forma")

    @staticmethod
    def buscarPorId(id):
        return CRUD.buscarId("forma", "ID_Forma", id)

    @staticmethod
    def atualizar(id, body_response):
        return CRUD.atualizar("forma", "ID_Forma", id, body_response)

    @staticmethod
    def deletar(id):
        return CRUD.deletar("forma", "ID_Forma", id)
