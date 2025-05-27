from pydantic import BaseModel, ConfigDict
from datetime import datetime

class Entrada(BaseModel):
    IDCodigo: int | None = None
    IDProduto: int
    Quantidade: float
    DataEntrada: datetime
    Fornecedor: str | None = None
    NotaFiscal: str | None = None
    Observacao: str | None = None

    model_config = ConfigDict(from_attributes=True)
