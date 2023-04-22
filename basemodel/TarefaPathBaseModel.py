from pydantic import BaseModel, Field


class TarefaPathBaseModel(BaseModel):
    id: int = Field(None, description='Identificador', example=1)
