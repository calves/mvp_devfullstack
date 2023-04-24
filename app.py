import flask
from flask import request, jsonify, json
from flask_cors import CORS
from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI

from basemodel.TarefaBaseModel import TarefaBaseModel
from basemodel.TarefaPathBaseModel import TarefaPathBaseModel
from model.Tarefa import Tarefa
from response.TarefaResponse import TarefaResponse
from service.TarefaService import TarefaService

info = Info(title="Tarefas API", version="1.0.0")
app = OpenAPI(__name__, info=info)
tarefas_tag = Tag(name="tarefa", description="Tarefas")
CORS(app)


@app.post('/tarefa/nova', summary="Criar nova tarefa", tags=[tarefas_tag])
def adicionar_tarefa(body: TarefaBaseModel):
    tarefa_request = request.json
    tarefa = Tarefa('', tarefa_request['titulo'], tarefa_request['descricao'], 'false', tarefa_request['data'])
    tarefa_gravada = TarefaService().gravar(tarefa)
    return criar_response(jsonify(tarefa_gravada.__dict__), 200)


@app.get('/tarefa/todas', summary="Listar todas as tarefas", tags=[tarefas_tag])
def listar_tarefas():
    tarefas = TarefaService().listar()
    schema = TarefaResponse(many=True)
    return jsonify(schema.dump(tarefas))


@app.put('/tarefa/finalizada/<int:id>', summary="Concluir uma tarefa", tags=[tarefas_tag])
def finalizar_tarefa_por_id(path: TarefaPathBaseModel):
    tarefa = Tarefa(path.id, '', '', '', '')
    status_code = TarefaService().finalizar(tarefa)
    if status_code == 200:
        mensagem = {'message': 'Tarefa concluida com sucesso'}
    else:
        mensagem = {'message': 'Tarefa nao encontrada'}

    return criar_response(mensagem, status_code)


@app.delete('/tarefa/removida/<int:id>', summary="Apagar tarefa por id", tags=[tarefas_tag])
def apagar_tarefa(path: TarefaPathBaseModel):
    tarefa = Tarefa(path.id, '', '', '', '')
    TarefaService().excluir(tarefa)
    return criar_response({'message': 'Tarefa removida com sucesso'}, 200)


def criar_response(body, status_code):
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    return flask.Response(status=status_code, response=json.dumps(body.json), headers=headers,
                          mimetype="application/json")


if __name__ == '__main__':
    app.run()
