from fastapi import APIRouter, Depends, HTTPException
from typing import List
from infrastructure.db.session import get_session
from infrastructure.db.repositories import ClienteRepositorySQLAlchemy
from core.entities.cliente import Cliente

router = APIRouter(prefix="/cliente", tags=["Cliente"])


def get_repo(session=Depends(get_session)):
    return ClienteRepositorySQLAlchemy(session)


@router.get("/", response_model=List[Cliente])
def list_clientes(repo=Depends(get_repo)):
    return repo.list_all()


@router.get("/{idcodigo}", response_model=Cliente)
def get_cliente(idcodigo: int, repo=Depends(get_repo)):
    item = repo.get_by_id(idcodigo)
    if not item:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return item


@router.post("/", response_model=Cliente)
def add_cliente(cliente: Cliente, repo=Depends(get_repo)):
    return repo.add(cliente)


@router.put("/{idcodigo}", response_model=Cliente)
def update_cliente(idcodigo: int, cliente: Cliente, repo=Depends(get_repo)):
    cliente.IDCodigo = idcodigo
    return repo.update(cliente)


@router.delete("/{idcodigo}")
def delete_cliente(idcodigo: int, repo=Depends(get_repo)):
    repo.delete(idcodigo)
    return {"ok": True}
