from pydantic import BaseModel
from models.enums import RoleType
from pydantic import EmailStr


class UserBase(BaseModel):
   email: EmailStr
   
class UserSchema(UserBase):
   lastName: str
   firstName: str
   role : RoleType

   class Config:
        orm_mode = True

class UserCreateSchema(UserSchema):
    hash_password: str

    class Config:
        orm_mode = False

