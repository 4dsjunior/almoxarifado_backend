# core/entities/forma_pagto.py
from pydantic import BaseModel, ConfigDict

class FormaPagto(BaseModel):
    IDCodigo: int | None = None
    Nome: str
    Observacao: str | None = None

    model_config = ConfigDict(from_attributes=True)
