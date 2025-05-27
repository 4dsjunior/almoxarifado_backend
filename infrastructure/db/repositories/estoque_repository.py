from sqlalchemy.orm import Session
from typing import List, Optional

from infrastructure.db.models.estoque import Tabela_TBEstoque
from core.entities.estoque import Estoque

class EstoqueRepositorySQLAlchemy:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Estoque]:
        db_obj = (
            self.session
            .query(Tabela_TBEstoque)
            .filter_by(IDCodigo=idcodigo)
            .first()
        )
        return Estoque.model_validate(db_obj) if db_obj else None

    def get_by_barcode(self, cod_de_barras: str) -> Optional[Estoque]:
        db_obj = (
            self.session
            .query(Tabela_TBEstoque)
            .filter_by(CodDeBarras=cod_de_barras)
            .first()
        )
        return Estoque.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Estoque]:
        objs = self.session.query(Tabela_TBEstoque).all()
        return [Estoque.model_validate(obj) for obj in objs]

    def add(self, item: Estoque) -> Estoque:
        db_obj = Tabela_TBEstoque(
            **item.model_dump(exclude_unset=True, exclude={"IDCodigo"})
        )
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Estoque.model_validate(db_obj)

    def update(self, item: Estoque) -> Estoque:
        db_obj = (
            self.session
            .query(Tabela_TBEstoque)
            .filter_by(IDCodigo=item.IDCodigo)
            .first()
        )
        if not db_obj:
            raise ValueError("Estoque não encontrado")
        for field, value in item.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return Estoque.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = (
            self.session
            .query(Tabela_TBEstoque)
            .filter_by(IDCodigo=idcodigo)
            .first()
        )
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()
