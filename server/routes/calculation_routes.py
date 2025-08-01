from fastapi import APIRouter, Depends

from server.models.calculation_model import CalculationInput
from server.utils.auth import get_current_user_id
from server.controllers.calculation_controller import calculate_profit

router = APIRouter()

@router.post("/calculate-profit")
async def calculate(data: CalculationInput, user_id: str = Depends(get_current_user_id)):
    return await calculate_profit(data, user_id)
