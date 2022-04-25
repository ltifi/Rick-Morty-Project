import os
from datetime import timedelta, datetime
from typing import Union, Optional

from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from config.database import SessionLocal
from jose import jwt, JWTError
from models.user import User
from functools import lru_cache
import config.config as config


session=SessionLocal()
SECRET_KEY=config.Settings().SECRET_KEY
print(SECRET_KEY)
ALGORITHM=config.Settings().ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES=config.Settings().ACCESS_TOKEN_EXPIRE_MINUTES
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def hash_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expires = datetime.utcnow() + expires_delta
    else:
        expires = datetime.utcnow() + timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expires})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()

def authenticate_user(email: str, password: str) -> Union[bool, User]:
    user: User = get_user_by_email(session, email)
    if not user:
        return False
    if not verify_password(password, user.hash_password):
        return False
    return user

