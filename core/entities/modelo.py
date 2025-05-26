from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Modelo(BaseModel):
    IDCodigo: int | None = None
    Nome: str

    model_config = ConfigDict(from_attributes=True)
