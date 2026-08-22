from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.core.security import hash_password, verify_password
from app.core.exceptions import BadRequestException,UnauthorizedException


def create_user(db: Session, user_data: UserCreate):
    # 1. Kiểm tra email tồn tại
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise BadRequestException("Email đã tồn tại")

    hashed_pwd = hash_password(user_data.password)

    new_user = User(
        email=user_data.email,
        hashed_password=hashed_pwd,
        full_name=user_data.full_name,
        role=user_data.role.upper()
    )

    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  

    return new_user

def authenticate_user(db: Session, user_data: UserLogin):
    user = db.query(User).filter(User.email == user_data.email).first()

    if not user or not verify_password(user_data.password, user.hashed_password):
        raise UnauthorizedException("Email hoặc mật khẩu không đúng")
    if not user.is_active : 
        raise UnauthorizedException("Tài khoản đã bị khóa")
    return user
