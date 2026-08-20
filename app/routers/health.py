from fastapi import APIRouter, Request
from app.schemas.ApiResponse import success_response
from app.core.exceptions import BadRequestException, ForbiddenException, NotFoundException


router = APIRouter(
    prefix="/api/health",
    tags=["Test Error"]
)


@router.get("/health")
def health_check(request: Request):
    return success_response(
        request=request,
        data={"status": "ok"},
        message="Service is healthy"
    )

@router.get("/test-400")
def test_400():
    raise BadRequestException("Test loi 400")

@router.get("/test-403")
def test_403():
    raise ForbiddenException("Test loi 403")

@router.get("/test-404")
def test_404():
    raise NotFoundException("Test loi 404")