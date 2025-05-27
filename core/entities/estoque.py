from pydantic import BaseModel, ConfigDict

class Estoque(BaseModel):
    IDCodigo: int | None = None
    CodDeBarras: str
    NomeProduto: str
    Descricao: str | None = None
    Categoria: str | None = None
    Marca: str | None = None
    Modelo: str | None = None
    QtdeEstoque: float
    Unidade: str | None = None
    Prateleira: str | None = None
    Almoxarifado: str | None = None
    Foto: str | None = None

    model_config = ConfigDict(from_attributes=True)
