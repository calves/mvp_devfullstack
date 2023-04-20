from flask import Flask, request, jsonify, json
from flask_openapi3 import OpenAPI, Info, Tag

from app.model.Tarefa import Tarefa
from app.response.TarefaResponse import TarefaResponse
from app.service.TarefaService import TarefaService

app = Flask(__name__)

info = Info(title="Listas de tarefas API", version="1.0.0")
app = OpenAPI(__name__, info=info)

tarefas_tag = Tag(name="tarefa", description="Tarefas")


@app.post('/tarefa/nova', summary="Criar nova tarefa", tags=[tarefas_tag])
def adicionar_tarefa():
    tarefa_request = request.json
    tarefa = Tarefa(1, tarefa_request['titulo'], tarefa_request['descricao'], 'false', tarefa_request['data'])
    tarefa_gravada = TarefaService().gravar(tarefa)
    return jsonify(tarefa_gravada.__dict__)


@app.get('/tarefa/todas', summary="Listar todas as tarefas", tags=[tarefas_tag])
def listar_tarefas():
    tarefas = TarefaService().listar()
    schema = TarefaResponse(many=True)
    return jsonify(schema.dump(tarefas))


@app.get('/tarefa/<int:id>', summary="Recuperar tarefa por id tarefa", tags=[tarefas_tag])
def recuperar_tarefa_por_id(id):
    tarefa = Tarefa(id, '', '', '', '')
    tarefa_recuperada = TarefaService().buscar_por_id(tarefa)
    return  json.dumps(tarefa_recuperada.__dict__), 200, {'ContentType': 'application/json'}


@app.put('/tarefa/finalizada/<int:id>', summary="Concluir uma tarefa por id", tags=[tarefas_tag])
def finalizar_tarefa_por_id(id):
    tarefa = Tarefa(id, '', '', '', '')
    TarefaService().finalizar(tarefa)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.delete('/tarefa/removida/<int:id>', summary="Apagar tarefa por id", tags=[tarefas_tag])
def apagar_tarefa(id):
    tarefa = Tarefa(id, '', '', '', '')
    TarefaService().excluir(tarefa)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

app.run()
