from app.dao.TarefaDao import TarefaDAO
from app.model.Tarefa import Tarefa
from app.util.Util import Util


class TarefaService:
    def __init__(self):
        self.tarefa_dao = TarefaDAO.get_instance()

    def gravar(self, tarefa: Tarefa):
        tarefa_gravada = self.tarefa_dao.inserir(tarefa)
        return tarefa_gravada

    def buscar_por_id(self, tarefa: Tarefa):
        tarefa_recuperada = self.tarefa_dao.buscar_por_id(tarefa)
        tarefa_recuperada.data = Util().formatar_data(tarefa_recuperada.data)
        return tarefa_recuperada

    def listar(self):
        tarefas = self.tarefa_dao.listar_todas()
        return tarefas

    def finalizar(self, tarefa):
        tarefa_recuperada = self.tarefa_dao.buscar_por_id(tarefa)
        tarefa_recuperada.status = True
        self.tarefa_dao.atualizar(tarefa_recuperada)

    def excluir(self, tarefa):
        tarefa_recuperada = self.tarefa_dao.buscar_por_id(tarefa)
        self.tarefa_dao.excluir(tarefa_recuperada)
