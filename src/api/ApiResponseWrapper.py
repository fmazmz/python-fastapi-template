from http import HTTPStatus
from uuid import UUID

from pydantic import BaseModel
from typing import Any

class ApiResponseWrapper(BaseModel):
    data: Any
    status_code: HTTPStatus
    operation_id: UUID
