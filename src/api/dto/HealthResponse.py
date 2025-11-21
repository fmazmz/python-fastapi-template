from pydantic import BaseModel

from src.api.utils.ApiResponseWrapper import ApiResponseWrapper


class HealthPayload(BaseModel):
    message: str

HealthResponse = ApiResponseWrapper[HealthPayload]