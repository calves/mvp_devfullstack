from dao.TarefaDao import TarefaDAO
from model.Tarefa import Tarefa


class TarefaService:
    def __init__(self):
        self.tarefa_dao = TarefaDAO.get_instance()

    def gravar(self, tarefa: Tarefa):
        tarefa_gravada = self.tarefa_dao.inserir(tarefa)
        return tarefa_gravada

    def listar(self):
        tarefas = self.tarefa_dao.listar_todas()
        return tarefas

    def finalizar(self, tarefa):
        tarefa_recuperada = self.tarefa_dao.buscar_por_id(tarefa)
        if tarefa_recuperada != None:
            tarefa_recuperada.status = True
            self.tarefa_dao.atualizar(tarefa_recuperada)
            return 200
        return 400

    def excluir(self, tarefa):
        tarefa_recuperada = self.tarefa_dao.buscar_por_id(tarefa)
        self.tarefa_dao.excluir(tarefa_recuperada)
