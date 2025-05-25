from fastapi import APIRouter, Depends, HTTPException
from typing import List
from infrastructure.db.repositories import FornecedorRepositorySQLAlchemy
from core.entities.fornecedor import Fornecedor
from infrastructure.db.session import get_session

router = APIRouter(prefix="/fornecedor", tags=["Fornecedor"])

def get_repo(session=Depends(get_session)):
    return FornecedorRepositorySQLAlchemy(session)

@router.get("/", response_model=List[Fornecedor])
def listar(repo=Depends(get_repo)):
    return repo.list_all()

@router.get("/{idcodigo}", response_model=Fornecedor)
def get_by_id(idcodigo: int, repo=Depends(get_repo)):
    obj = repo.get_by_id(idcodigo)
    if not obj:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return obj

@router.post("/", response_model=Fornecedor)
def add(item: Fornecedor, repo=Depends(get_repo)):
    return repo.add(item)

@router.put("/{idcodigo}", response_model=Fornecedor)
def update(idcodigo: int, item: Fornecedor, repo=Depends(get_repo)):
    item.IDCodigo = idcodigo
    return repo.update(item)

@router.delete("/{idcodigo}")
def delete(idcodigo: int, repo=Depends(get_repo)):
    repo.delete(idcodigo)
    return {"ok": True}
