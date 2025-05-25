from fastapi import APIRouter, Depends, HTTPException
from typing import List
from infrastructure.db.repositories import ModeloRepositorySQLAlchemy
from core.entities.modelo import Modelo
from infrastructure.db.session import get_session

router = APIRouter(prefix="/modelo", tags=["Modelo"])

def get_repo(session=Depends(get_session)):
    return ModeloRepositorySQLAlchemy(session)

@router.get("/", response_model=List[Modelo])
def listar(repo=Depends(get_repo)):
    return repo.list_all()

@router.get("/{idcodigo}", response_model=Modelo)
def get_by_id(idcodigo: int, repo=Depends(get_repo)):
    obj = repo.get_by_id(idcodigo)
    if not obj:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")
    return obj

@router.post("/", response_model=Modelo)
def add(item: Modelo, repo=Depends(get_repo)):
    return repo.add(item)

@router.put("/{idcodigo}", response_model=Modelo)
def update(idcodigo: int, item: Modelo, repo=Depends(get_repo)):
    item.IDCodigo = idcodigo
    return repo.update(item)

@router.delete("/{idcodigo}")
def delete(idcodigo: int, repo=Depends(get_repo)):
    repo.delete(idcodigo)
    return {"ok": True}
