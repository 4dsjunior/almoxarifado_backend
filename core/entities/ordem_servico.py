# core/entities/ordem_servico.py
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class OrdemServico(BaseModel):
    IDCodigo: int | None = None
    Numero: str
    Descricao: str | None = None
    Solicitante: str | None = None
    DataAbertura: datetime | None = None
    DataFechamento: datetime | None = None
    Status: str | None = None

    model_config = ConfigDict(from_attributes=True)
