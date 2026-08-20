from datetime import datetime, timezone
from fastapi import Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.schemas.ApiResponse import APIResponse


class BadRequestException(HTTPException):
    def __init__(self, detail: str = "Yeu cau khong hop le"):
        super().__init__(status_code=400, detail=detail)


class ForbiddenException(HTTPException):
    def __init__(self, detail: str = "Khong co quyen truy cap"):
        super().__init__(status_code=403, detail=detail)


class NotFoundException(HTTPException):
    def __init__(self, detail: str = "Khong tim thay tai nguyen"):
        super().__init__(status_code=404, detail=detail)


def http_exception_handler(request: Request, exc: HTTPException):
    response_model = APIResponse(
        success=False,
        statusCode=exc.status_code,
        message=str(exc.detail),
        timestamp=datetime.now(timezone.utc).isoformat(),
        path=request.url.path
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=response_model.model_dump(mode="json")
    )


def validation_exception_handler(request: Request, exc: RequestValidationError):
    response_model = APIResponse(
        success=False,
        statusCode=422,
        message="Du lieu khong hop le",
        errors=exc.errors(),
        timestamp=datetime.now(timezone.utc).isoformat(),
        path=request.url.path
    )
    return JSONResponse(
        status_code=422,
        content=response_model.model_dump(mode="json")
    )