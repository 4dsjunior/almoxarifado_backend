from sqlalchemy.orm import Session
from infrastructure.db.models.categoria import Tabela_TBCategorias
from core.entities.categoria import Categoria
from typing import List, Optional


class CategoriaRepositorySQLAlchemy:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Categoria]:
        db_obj = self.session.query(Tabela_TBCategorias).filter_by(
            IDCodigo=idcodigo).first()
        return Categoria.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Categoria]:
        objs = self.session.query(Tabela_TBCategorias).all()
        return [Categoria.model_validate(obj) for obj in objs]

    def add(self, categoria: Categoria) -> Categoria:
        db_obj = Tabela_TBCategorias(
            **categoria.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Categoria.model_validate(db_obj)

    def update(self, categoria: Categoria) -> Categoria:
        db_obj = self.session.query(Tabela_TBCategorias).filter_by(
            IDCodigo=categoria.IDCodigo).first()
        if not db_obj:
            raise ValueError("Categoria não encontrada")
        for field, value in categoria.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return Categoria.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = self.session.query(Tabela_TBCategorias).filter_by(
            IDCodigo=idcodigo).first()
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()
