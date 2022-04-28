""" User model."""

from sqlalchemy import Column, Integer, String, Enum
from config.database import engine, Base
from models.enums import RoleType

class User(Base):
    """ Create user model."""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    lastName = Column(String(115), unique=False, index=False, nullable=True)
    firstName = Column(String(115), unique=False, index=False, nullable=True)
    email = Column(String(115), unique=False, index=False, nullable=True)
    hash_password=Column(String(115), unique=False, index=False, nullable=True)
    role=Column(Enum(RoleType))

Base.metadata.create_all(engine)
