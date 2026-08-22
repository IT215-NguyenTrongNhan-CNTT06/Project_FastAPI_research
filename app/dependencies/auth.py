from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.core.config import settings
from app.core.exceptions import UnauthorizedException, ForbiddenException, NotFoundException

reusable_oauth2 = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(reusable_oauth2),
    db: Session = Depends(get_db)
) -> User:
    token = credentials.credentials

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise UnauthorizedException("Khong the xac thuc thong tin dang nhap")
    except jwt.ExpiredSignatureError:
        raise UnauthorizedException("Phien dang nhap da het han, vui long dang nhap lai")
    except jwt.PyJWTError:
        raise UnauthorizedException("Khong the xac thuc thong tin dang nhap")

    user = db.query(User).filter(User.email == email).first()

    if user is None:
        raise NotFoundException("Nguoi dung khong ton tai")

    if not user.is_active:
        raise ForbiddenException("Tai khoan nay da bi tam khoa")

    return user


def require_admin(current_user: User = Depends(get_current_user)) -> User:
    if current_user.role != "ADMIN":
        raise ForbiddenException("Chi Admin moi co quyen truy cap")
    return current_user