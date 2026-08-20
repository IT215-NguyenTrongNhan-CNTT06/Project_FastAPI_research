from datetime import datetime, timezone
from typing import Any, Optional
from pydantic import BaseModel
from fastapi import Request
from fastapi.responses import JSONResponse


class APIResponse(BaseModel):
    success: bool
    statusCode: int
    message: str
    data: Optional[Any] = None
    errors: Optional[Any] = None
    timestamp: str
    path: str



def success_response(
    request: Request,
    data: Any = None,
    message: str = "Thanh cong",
    code: int = 200
) -> JSONResponse:
    response_model = APIResponse(
        success=True,
        statusCode=code,
        message=message,
        data=data,
        timestamp=datetime.now(timezone.utc).isoformat(),
        path=request.url.path
    )
    return JSONResponse(
        status_code=code,
        content=response_model.model_dump(mode="json")
    )


def created_response(
    request: Request,
    data: Any = None,
    message: str = "Tao moi thanh cong"
) -> JSONResponse:
    return success_response(request=request, data=data, message=message, code=201)