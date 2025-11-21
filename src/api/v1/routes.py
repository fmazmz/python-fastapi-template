from fastapi import APIRouter
from uuid import uuid4

router = APIRouter(prefix="/api", tags=["template"])

@router.get("/health", response_model=APIResponse)
def health_check():
    return {
        "status_code": 200,
        "operation_id": uuid4(),
        "data": "ok"
    }
