""" User Schema ."""

from pydantic import BaseModel
from pydantic import EmailStr
from models.enums import RoleType

class UserBase(BaseModel):
    """ User Base Schema ."""
    email: EmailStr

class UserSchema(UserBase):
    """ User Schema ."""
    lastName: str
    firstName: str
    role : RoleType

    class Config:
        """ User Config Schema ."""
        orm_mode = True

class UserCreateSchema(UserSchema):
    """ User Create Schema ."""
    hash_password: str

    class Config:
        """ User Config Schema ."""
        orm_mode = False

class UserAllSchema(UserSchema):
    """ User Schema with id ."""
    id: int

    class Config:
        """ User Config Schema ."""
        orm_mode = True
