from fastapi import APIRouter, Depends, HTTPException
from typing import List
from infrastructure.db.repositories import MarcaRepositorySQLAlchemy
from core.entities.marca import Marca
from infrastructure.db.session import get_session

router = APIRouter(prefix="/marca", tags=["Marca"])

def get_repo(session=Depends(get_session)):
    return MarcaRepositorySQLAlchemy(session)

@router.get("/", response_model=List[Marca])
def listar(repo=Depends(get_repo)):
    return repo.list_all()

@router.get("/{idcodigo}", response_model=Marca)
def get_by_id(idcodigo: int, repo=Depends(get_repo)):
    obj = repo.get_by_id(idcodigo)
    if not obj:
        raise HTTPException(status_code=404, detail="Marca não encontrada")
    return obj

@router.post("/", response_model=Marca)
def add(item: Marca, repo=Depends(get_repo)):
    return repo.add(item)

@router.put("/{idcodigo}", response_model=Marca)
def update(idcodigo: int, item: Marca, repo=Depends(get_repo)):
    item.IDCodigo = idcodigo
    return repo.update(item)

@router.delete("/{idcodigo}")
def delete(idcodigo: int, repo=Depends(get_repo)):
    repo.delete(idcodigo)
    return {"ok": True}
