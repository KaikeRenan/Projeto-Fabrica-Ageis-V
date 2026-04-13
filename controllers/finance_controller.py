from fastapi import APIRouter, HTTPException, Query
from dtos.finance_dto import FinanceResponseDTO
from repositories.finance_repository import FinanceRepository
from services.finance_service import FinanceService

router = APIRouter()
repo = FinanceRepository()
service = FinanceService(repo)

@router.get("/get-valuation", response_model=FinanceResponseDTO)
def get_valuation(url: str = Query(...)):
    try:
        entity = service.execute(url)
        return FinanceResponseDTO(  
            ticker=entity.ticker,
            nome_empresa=entity.nome_empresa, 
            dados=entity.dados
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))