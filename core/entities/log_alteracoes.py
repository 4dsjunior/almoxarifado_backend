from pydantic import BaseModel, ConfigDict
from datetime import datetime


class LogAlteracoes(BaseModel):
    IDCodigo: int | None = None
    Tabela: str
    Acao: str
    DataHora: datetime
    Usuario: str | None = None
    Descricao: str | None = None

    model_config = ConfigDict(from_attributes=True)
