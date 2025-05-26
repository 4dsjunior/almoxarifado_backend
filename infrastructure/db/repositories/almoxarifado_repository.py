from sqlalchemy.orm import Session
from infrastructure.db.models.almoxarifado import Tabela_TBAlmoxarifados
from core.entities.almoxarifado import Almoxarifado
from typing import List, Optional


class AlmoxarifadoRepositorySQLAlchemy:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Almoxarifado]:
        db_obj = self.session.query(Tabela_TBAlmoxarifados).filter_by(
            IDCodigo=idcodigo).first()
        return Almoxarifado.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Almoxarifado]:
        objs = self.session.query(Tabela_TBAlmoxarifados).all()
        return [Almoxarifado.model_validate(obj) for obj in objs]

    def add(self, almoxarifado: Almoxarifado) -> Almoxarifado:
        db_obj = Tabela_TBAlmoxarifados(
            **almoxarifado.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Almoxarifado.model_validate(db_obj)

    def update(self, almoxarifado: Almoxarifado) -> Almoxarifado:
        db_obj = self.session.query(Tabela_TBAlmoxarifados).filter_by(
            IDCodigo=almoxarifado.IDCodigo).first()
        if not db_obj:
            raise ValueError("Almoxarifado não encontrado")
        for field, value in almoxarifado.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return Almoxarifado.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = self.session.query(Tabela_TBAlmoxarifados).filter_by(
            IDCodigo=idcodigo).first()
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()
