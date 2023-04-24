import psycopg2

from model.Tarefa import Tarefa


class TarefaDAO:
    __instance = None

    @staticmethod
    def get_instance():
        if TarefaDAO.__instance is None:
            TarefaDAO()
        return TarefaDAO.__instance

    def __init__(self):
        if TarefaDAO.__instance is not None:
            return TarefaDAO.__instance
        else:
            TarefaDAO.__instance = self
            self.conn = psycopg2.connect(
                host='localhost',
                port=5432,
                database='tarefas_db',
                user='postgres',
                password='postgres'
            )
            self.conecta = self.conn.cursor()
            self.conecta.execute('''CREATE TABLE IF NOT EXISTS tarefa 
                            (id SERIAL PRIMARY KEY, 
                            titulo TEXT, 
                            descricao VARCHAR(200), 
                            status bool, 
                            data   timestamp)''')
            self.conn.commit()            
            
            
    def inserir(self, tarefa: Tarefa):
        self.conectar()
        self.conecta.execute(
            "INSERT INTO tarefa (titulo, descricao, status, data) VALUES (%s, %s, %s, %s) RETURNING id",
            (tarefa.titulo, tarefa.descricao, tarefa.status, tarefa.data))
        pk = self.conecta.fetchone()[0]
        tarefa.id = pk
        self.conn.commit()
        self.conecta.close()
        return tarefa

    def atualizar(self, tarefa: Tarefa):
        self.conectar()
        self.conecta.execute("UPDATE tarefa SET titulo=%s, descricao=%s, status=%s, data=%s WHERE id=%s",
                             (tarefa.titulo, tarefa.descricao, tarefa.status, tarefa.data, tarefa.id))
        self.conn.commit()
        self.conecta.close()

    def excluir(self, tarefa: Tarefa):
        self.conectar()
        self.conecta.execute("DELETE FROM tarefa WHERE id=%s", (tarefa.id,))
        self.conn.commit()
        self.conecta.close()

    def buscar_por_id(self, tarefa: Tarefa):
        self.conectar()
        self.conecta.execute("SELECT * FROM tarefa WHERE id=%s", (tarefa.id,))
        row = self.conecta.fetchone()
        if row is not None:
            tarefa = Tarefa(row[0], row[1], row[2], row[3], row[4])
            self.conecta.close()
            return tarefa
        else:
            self.conecta.close()
            return None

    def listar_todas(self):
        self.conectar()
        tarefas = []
        self.conecta.execute("SELECT * FROM tarefa order by data, status")
        rows = self.conecta.fetchall()

        for row in rows:
            tarefa = Tarefa(row[0], row[1], row[2], row[3], row[4])
            tarefas.append(tarefa)

        self.conecta.close()
        return tarefas

    def conectar(self):
        if self.conecta.closed:
            self.conecta = self.conn.cursor()
