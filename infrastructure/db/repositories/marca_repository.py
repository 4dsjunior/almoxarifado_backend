from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException

from infrastructure.db.models.marca import Tabela_TBMarca
from core.entities.marca import Marca
from core.entities.repositories import Protocol  # ajuste conforme import real

class MarcaRepositorySQLAlchemy:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Marca]:
        db_obj = (
            self.session
            .query(Tabela_TBMarca)
            .filter_by(IDCodigo=idcodigo)
            .first()
        )
        return Marca.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Marca]:
        objs = self.session.query(Tabela_TBMarca).all()
        return [Marca.model_validate(obj) for obj in objs]

    def add(self, marca: Marca) -> Marca:
        db_obj = Tabela_TBMarca(**marca.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Marca.model_validate(db_obj)

    def update(self, marca: Marca) -> Marca:
        db_obj = (
            self.session
            .query(Tabela_TBMarca)
            .filter_by(IDCodigo=marca.IDCodigo)
            .first()
        )
        if not db_obj:
            raise HTTPException(status_code=404, detail="Marca não encontrada")
        for field, value in marca.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return Marca.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = (
            self.session
            .query(Tabela_TBMarca)
            .filter_by(IDCodigo=idcodigo)
            .first()
        )
        if not db_obj:
            raise HTTPException(status_code=404, detail="Marca não encontrada")
        self.session.delete(db_obj)
        self.session.commit()
