""" User crud file."""

from typing import List
from sqlalchemy.orm import Session
from security.security import hash_password
from schemas.user_schema import UserCreateSchema, UserSchema
from models.user import User

def add_user(session: Session, user_data: UserCreateSchema):
    """ Create a new user."""
    hashed_password = hash_password(user_data.hash_password)
    db_user_info = User(
        email=user_data.email,
        lastName=user_data.lastName,
        firstName=user_data.firstName,
        hash_password=hashed_password,
        role=user_data.role)
    session.add(db_user_info)
    session.commit()
    session.refresh(db_user_info)
    return db_user_info

def get_all_users(session: Session) -> List[UserSchema]:
    """ Get all users."""
    return session.query(User).all()
