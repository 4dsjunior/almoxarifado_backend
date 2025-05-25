from fastapi import APIRouter, Depends, HTTPException
from typing import List

from core.entities.estoque import Estoque
from infrastructure.db.session import get_session
from infrastructure.db.repositories import EstoqueRepositorySQLAlchemy

router = APIRouter(prefix="/estoque", tags=["Estoque"])

def get_estoque_repo(session=Depends(get_session)):
    return EstoqueRepositorySQLAlchemy(session)

@router.get("/", response_model=List[Estoque])
def listar_estoque(repo=Depends(get_estoque_repo)):
    return repo.list_all()

@router.get("/{idcodigo}", response_model=Estoque)
def get_estoque(idcodigo: int, repo=Depends(get_estoque_repo)):
    item = repo.get_by_id(idcodigo)
    if not item:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return item

@router.post("/", response_model=Estoque)
def add_estoque(item: Estoque, repo=Depends(get_estoque_repo)):
    return repo.add(item)

@router.put("/{idcodigo}", response_model=Estoque)
def update_estoque(idcodigo: int, item: Estoque, repo=Depends(get_estoque_repo)):
    item.IDCodigo = idcodigo
    return repo.update(item)

@router.delete("/{idcodigo}")
def delete_estoque(idcodigo: int, repo=Depends(get_estoque_repo)):
    repo.delete(idcodigo)
    return {"ok": True}
