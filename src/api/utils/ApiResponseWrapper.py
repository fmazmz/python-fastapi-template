from http import HTTPStatus
from typing import Generic, TypeVar
from uuid import UUID

from pydantic import BaseModel, Field



T = TypeVar("T")

class ApiResponseWrapper(BaseModel, Generic[T]):
    data: T
    status_code: HTTPStatus = Field(..., description="HTTP status code")
    operation_id: UUID = Field(..., description="Unique operation identifier")