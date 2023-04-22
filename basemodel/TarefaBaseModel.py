from typing import Optional

from pydantic.fields import Field
from pydantic.main import BaseModel


class TarefaBaseModel(BaseModel):
    id: Optional[int] = Field(None, description='Identificador', example=1)
    titulo: str = Field(None, description='Titulo da tarefa', example='MVP Pos')
    descricao: str = Field(None, description='Descricao da tarefa', example='Entregar o MVP')
    status: bool = Field(None, description='Status da tarefa', example='false')
    data: str = Field(None, description='Data para realizacao da terafa (yyyy-MM-dd HH:mm:ss)',
                      example='2023-04-30 20:40:59')
