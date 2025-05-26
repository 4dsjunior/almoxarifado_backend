from sqlalchemy.orm import Session
from infrastructure.db.models.cliente import Tabela_TBClientes
from core.entities.cliente import Cliente
from typing import List, Optional


class ClienteRepositorySQLAlchemy:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, idcodigo: int) -> Optional[Cliente]:
        db_obj = self.session.query(Tabela_TBClientes).filter_by(
            IDCodigo=idcodigo).first()
        return Cliente.model_validate(db_obj) if db_obj else None

    def list_all(self) -> List[Cliente]:
        objs = self.session.query(Tabela_TBClientes).all()
        return [Cliente.model_validate(obj) for obj in objs]

    def add(self, cliente: Cliente) -> Cliente:
        db_obj = Tabela_TBClientes(
            **cliente.model_dump(exclude_unset=True, exclude={"IDCodigo"}))
        self.session.add(db_obj)
        self.session.commit()
        self.session.refresh(db_obj)
        return Cliente.model_validate(db_obj)

    def update(self, cliente: Cliente) -> Cliente:
        db_obj = self.session.query(Tabela_TBClientes).filter_by(
            IDCodigo=cliente.IDCodigo).first()
        if not db_obj:
            raise ValueError("Cliente não encontrado")
        for field, value in cliente.model_dump(exclude_unset=True, exclude={"IDCodigo"}).items():
            setattr(db_obj, field, value)
        self.session.commit()
        return Cliente.model_validate(db_obj)

    def delete(self, idcodigo: int) -> None:
        db_obj = self.session.query(Tabela_TBClientes).filter_by(
            IDCodigo=idcodigo).first()
        if db_obj:
            self.session.delete(db_obj)
            self.session.commit()
