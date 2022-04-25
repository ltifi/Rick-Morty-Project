from typing import List
from sqlalchemy.orm import Session
from security.security import hash_password
from schemas.user import UserCreateSchema, UserSchema
from models.user import User

def add_user(db: Session, user_data: UserCreateSchema):
    hashed_password = hash_password(user_data.hash_password)
    db_user = User(
        email=user_data.email,
        lastName=user_data.lastName,
        firstName=user_data.firstName,
        hash_password=hashed_password,
        role=user_data.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_users(db: Session) -> List[UserSchema]:
    return db.query(User).all()