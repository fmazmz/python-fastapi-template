from http import HTTPStatus

from fastapi import APIRouter
from uuid import uuid4

from src.api.ApiResponseWrapper import ApiResponseWrapper

router = APIRouter(prefix="/api", tags=["template"])

@router.get("/health", response_model=ApiResponseWrapper)
def health_check():
    return {
        "status_code": HTTPStatus.OK,
        "operation_id": uuid4(),
        "data": "ok"
    }
