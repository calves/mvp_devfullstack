from datetime import datetime
class Tarefa:
    def __init__(self, id: int, titulo: str, descricao: str, status: bool, data: datetime):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data = data

    def __str__(self):
        return f"Tarefa(id={self.id}, 'titulo={self.titulo}', 'descricao={self.descricao}', 'status={self.status}', 'data={self.data}')"
