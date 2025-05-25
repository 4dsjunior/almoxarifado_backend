from fastapi import APIRouter, Depends, HTTPException
from typing import List
from infrastructure.db.session import get_session
from infrastructure.db.repositories import OrdemServicoProdutoRepositorySQLAlchemy
from core.entities.ordem_servico_produto import OrdemServicoProduto

router = APIRouter(prefix="/os-produto", tags=["Ordem de Serviço Produto"])


def get_repo(session=Depends(get_session)):
    return OrdemServicoProdutoRepositorySQLAlchemy(session)


@router.get("/", response_model=List[OrdemServicoProduto])
def list_all(repo=Depends(get_repo)):
    return repo.list_all()


@router.get("/{idcodigo}", response_model=OrdemServicoProduto)
def get_by_id(idcodigo: int, repo=Depends(get_repo)):
    item = repo.get_by_id(idcodigo)
    if not item:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    return item


@router.post("/", response_model=OrdemServicoProduto)
def add(item: OrdemServicoProduto, repo=Depends(get_repo)):
    return repo.add(item)


@router.put("/{idcodigo}", response_model=OrdemServicoProduto)
def update(idcodigo: int, item: OrdemServicoProduto, repo=Depends(get_repo)):
    item.IDCodigo = idcodigo
    return repo.update(item)


@router.delete("/{idcodigo}")
def delete(idcodigo: int, repo=Depends(get_repo)):
    repo.delete(idcodigo)
    return {"ok": True}


@router.get("/by-os/{id_ordem}", response_model=List[OrdemServicoProduto])
def list_by_ordem_servico(id_ordem: int, repo=Depends(get_repo)):
    return repo.list_by_ordem_servico(id_ordem)
