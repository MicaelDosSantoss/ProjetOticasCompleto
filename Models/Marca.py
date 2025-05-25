from uuid import uuid4
from Models.CRUD import CRUD

class Marca(CRUD):

    def __init__(self, Nome=None, ID_Marca=None):
        self.ID_Marca = ID_Marca if ID_Marca else str(uuid4())
        self.Nome = Nome

    def salvar(self):
        self.registar("marca", "ID_Marca")

    def mostrarTudo(self):
        self.mostrar("marca", "ID_Marca")

    @staticmethod
    def buscarPorId(id):
        return CRUD.buscarId("marca", "ID_Marca", id)

    @staticmethod
    def atualizar(id, body_response):
        return CRUD.atualizar("marca", "ID_Marca", id, body_response)

    @staticmethod
    def deletar(id):
        return CRUD.deletar("marca", "ID_Marca", id)


