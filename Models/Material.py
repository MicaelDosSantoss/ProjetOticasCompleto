from uuid import uuid4
from Models.CRUD import CRUD

class Material(CRUD):
    def __init__(self, Nome=None, ID_Material=None):
        self.ID_Material = ID_Material if ID_Material else str(uuid4())
        self.Nome = Nome

    def salvar(self):
        self.registar("material","ID_Material")

    def mostrarTudo(self):
        self.mostrar("material","ID_Material")

    @staticmethod
    def buscarPorId(id):
        return CRUD.buscarId("material", "ID_Material", id)

    @staticmethod
    def atualizar(id, body_response):
        return CRUD.atualizar("material", "ID_Material", id, body_response)

    @staticmethod
    def deletar(id):
        return CRUD.deletar("material", "ID_Material", id)