from http import HTTPStatus
from fastapi import APIRouter

from src.api.dto.HealthResponse import HealthResponse, HealthPayload
from src.api.utils.op_id_generator import generate_op_id


router = APIRouter(prefix="/api", tags=["template"])

@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return HealthResponse(
        data=HealthPayload(message="OK"),
        status_code=HTTPStatus.OK,
        operation_id=generate_op_id()
    )
