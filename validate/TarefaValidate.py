from model.Tarefa import Tarefa


class TarefaValidate:

    def validar(self, tarefa: Tarefa):
        erros: str = []
        if tarefa.titulo == "":
            erros.append('Campo titulo obrigatorio')

        if tarefa.descricao == "":
            erros.append('Campo descricao obrigatorio')

        if tarefa.data == "":
            erros.append('Campo data obrigatorio')

        return erros
