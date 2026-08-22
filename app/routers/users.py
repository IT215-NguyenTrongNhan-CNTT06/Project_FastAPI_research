from fastapi import APIRouter, Depends, Request, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse
from app.schemas.ApiResponse import success_response
from app.dependencies.auth import get_current_user, require_admin

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.get("/me")
def get_me(request: Request, current_user: User = Depends(get_current_user)):
    return success_response(
        request=request,
        data=UserResponse.model_validate(current_user).model_dump(mode="json"),
        message="Lay thong tin thanh cong"
    )


@router.get("")
def list_users(
    request: Request,
    search: Optional[str] = Query(None, description="Tim theo ten hoac email"),
    is_active: Optional[bool] = Query(None, description="Loc theo trang thai"),
    db: Session = Depends(get_db),
    _: User = Depends(require_admin)
):
    query = db.query(User)

    if search:
        query = query.filter(
            (User.full_name.ilike(f"%{search}%")) | (User.email.ilike(f"%{search}%"))
        )
    if is_active is not None:
        query = query.filter(User.is_active == is_active)

    users = query.all()
    data = [UserResponse.model_validate(u).model_dump(mode="json") for u in users]

    return success_response(request=request, data=data, message="Lay danh sach thanh cong")