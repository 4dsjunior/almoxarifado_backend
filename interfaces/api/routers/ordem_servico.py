from fastapi import APIRouter, Depends, HTTPException
from typing import List
from infrastructure.db.session import get_session
from infrastructure.db.repositories import OrdemServicoRepositorySQLAlchemy
from core.entities.ordem_servico import OrdemServico

router = APIRouter(prefix="/os", tags=["Ordem de Serviço"])


def get_repo(session=Depends(get_session)):
    return OrdemServicoRepositorySQLAlchemy(session)


@router.get("/", response_model=List[OrdemServico])
def list_os(repo=Depends(get_repo)):
    return repo.list_all()


@router.get("/{idcodigo}", response_model=OrdemServico)
def get_os(idcodigo: int, repo=Depends(get_repo)):
    item = repo.get_by_id(idcodigo)
    if not item:
        raise HTTPException(
            status_code=404, detail="Ordem de Serviço não encontrada")
    return item


@router.post("/", response_model=OrdemServico)
def add_os(os: OrdemServico, repo=Depends(get_repo)):
    return repo.add(os)


@router.put("/{idcodigo}", response_model=OrdemServico)
def update_os(idcodigo: int, os: OrdemServico, repo=Depends(get_repo)):
    os.IDCodigo = idcodigo
    return repo.update(os)


@router.delete("/{idcodigo}")
def delete_os(idcodigo: int, repo=Depends(get_repo)):
    repo.delete(idcodigo)
    return {"ok": True}
