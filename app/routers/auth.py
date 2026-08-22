from fastapi import APIRouter, Depends, Request, Form
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.schemas.ApiResponse import success_response, created_response
from app.db.database import get_db
from app.services import services
from pydantic import ValidationError
from app.core.security import create_access_token
from app.core.exceptions import BadRequestException

router = APIRouter(prefix="/api/auth", tags=["Authentication"])


@router.post("/register")
def register(
    email: str = Form(..., description="Email cua nguoi dung"),
    password: str = Form(..., description="Mat khau"),
    full_name: str = Form(..., description="Ho ten"),
    role: str = Form("USER", description="Vai tro: USER hoac ADMIN"),
    request: Request = None,
    db: Session = Depends(get_db)
):
    user_data = UserCreate(
        email=email,
        password=password,
        full_name=full_name,
        role=role
    )
    new_user = services.create_user(db=db, user_data=user_data)
    return created_response(
        request=request,
        data=UserResponse.model_validate(new_user).model_dump(mode="json"),
        message="Dang ky thanh cong"
    )


@router.post("/login")
def login(
    email: str = Form(..., description="Email cua nguoi dung"),
    password: str = Form(..., description="Mat khau"),
    request: Request = None,
    db: Session = Depends(get_db)
):
    try:
        user_data = UserLogin(email=email, password=password)
    except ValidationError:
        raise BadRequestException("Email khong dung dinh dang")
    
    user_data = UserLogin(email=email, password=password)
    user = services.authenticate_user(db=db, user_data=user_data)
    access_token = create_access_token(data={"sub": user.email, "id": user.id, "role": user.role})

    return success_response(
        request=request,
        data={
            "access_token": access_token,
            "token_type": "bearer",
            "user": UserResponse.model_validate(user).model_dump(mode="json")
        },
        message="Dang nhap thanh cong"
    )