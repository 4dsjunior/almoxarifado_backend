from fastapi import APIRouter, Depends, HTTPException
from typing import List
from infrastructure.db.repositories import CategoriaRepositorySQLAlchemy
from core.entities.categoria import Categoria
from infrastructure.db.session import get_session

router = APIRouter(prefix="/categoria", tags=["Categoria"])

def get_repo(session=Depends(get_session)):
    return CategoriaRepositorySQLAlchemy(session)

@router.get("/", response_model=List[Categoria])
def listar(repo=Depends(get_repo)):
    return repo.list_all()

@router.get("/{idcodigo}", response_model=Categoria)
def get_by_id(idcodigo: int, repo=Depends(get_repo)):
    obj = repo.get_by_id(idcodigo)
    if not obj:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return obj

@router.post("/", response_model=Categoria)
def add(item: Categoria, repo=Depends(get_repo)):
    return repo.add(item)

@router.put("/{idcodigo}", response_model=Categoria)
def update(idcodigo: int, item: Categoria, repo=Depends(get_repo)):
    item.IDCodigo = idcodigo
    return repo.update(item)

@router.delete("/{idcodigo}")
def delete(idcodigo: int, repo=Depends(get_repo)):
    repo.delete(idcodigo)
    return {"ok": True}
