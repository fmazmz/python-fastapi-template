from http import HTTPStatus
from fastapi import APIRouter

from src.api.ApiResponseWrapper import ApiResponseWrapper
from src.api.utils.op_id_generator import generate_op_id


router = APIRouter(prefix="/api", tags=["template"])

@router.get("/health", response_model=ApiResponseWrapper)
def health_check():
    return {
        "status_code": HTTPStatus.OK,
        "operation_id": generate_op_id(),
        "data": "ok"
    }
