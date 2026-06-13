from fastapi import APIRouter, HTTPException, Query
from dtos.finance_dto import FinanceResponseDTO
from repositories.finance_repository import FinanceRepository
from services.finance_service import FinanceService
from services.financeHealthAnalyze_service import FinancialHealthService

from analyzers.financeHealthAnalyzer import FinancialHealthAnalyzer

router = APIRouter()
repo = FinanceRepository()
finance_service = FinanceService(repo)
analyzer = FinancialHealthAnalyzer()

financeHealth_service = FinancialHealthService(repo, analyzer)



@router.get("/finance", response_model=FinanceResponseDTO)
def get_valuation(input_data: str = Query(..., description="Cole a URL do Google Finance ou o Ticker (ex: META:NASDAQ)")):
    try:
        entity = finance_service.execute(input_data)
        return FinanceResponseDTO(  
            ticker=entity.ticker,
            nome_empresa=entity.nome_empresa, 
            dados=entity.dados
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/finance/{ticker}/health")
def analyze_financial_health(ticker: str):
    try:
        result =financeHealth_service.execute(ticker)
        return {"ticker": ticker, "health_analysis": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))