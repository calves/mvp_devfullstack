from marshmallow import Schema, fields


class TarefaResponse(Schema):
    id = fields.Int()
    titulo = fields.Str()
    descricao = fields.Str()
    status = fields.Str()
    data = fields.Str()
