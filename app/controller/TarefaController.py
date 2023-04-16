from flask import Flask, request, jsonify

from app.model.Tarefa import Tarefa
from app.response.TarefaResponse import TarefaResponse
from app.service.TarefaService import TarefaService

app = Flask(__name__)


@app.route('/tarefa/nova', methods=['POST'])
def adicionar_tarefa():
    tarefa_request = request.json
    tarefa = Tarefa(1, tarefa_request['titulo'], tarefa_request['descricao'], 'false', tarefa_request['data'])
    tarefa_gravada = TarefaService().gravar(tarefa)
    return jsonify(tarefa_gravada.__dict__)

@app.route('/tarefa/todas', methods=['GET'])
def listar_tarefas():
    tarefas = TarefaService().listar()
    schema = TarefaResponse(many=True)
    return jsonify(schema.dump(tarefas))

@app.route('/tarefa/<int:id>', methods=['GET'])
def recuperar_tarefa_por_id(id):
    tarefa = Tarefa(id, '', '', '', '')
    tarefa_recuperada = TarefaService().buscar_por_id(tarefa)
    return  json.dumps(tarefa_recuperada.__dict__), 200, {'ContentType': 'application/json'}

@app.route('/tarefa/finalizada/<int:id>', methods=['PUT'])
def finalizar_tarefa_por_id(id):
    tarefa = Tarefa(id, '', '', '', '')
    TarefaService().finalizar(tarefa)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/tarefa/removida/<int:id>', methods=['DELETE'])
def apagar_tarefa(id):
    tarefa = Tarefa(id, '', '', '', '')
    TarefaService().excluir(tarefa)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

app.run()
