""" Comment Schema ."""

from typing import Optional
from pydantic import BaseModel
from models.enums import StatusType, CommentType

class CommentBase(BaseModel):
    """ Comment Bsae Schema ."""
    character_id: Optional[int] = None
    episode_id : Optional[int] = None
    comment : str

class EpisodeComment(BaseModel):
    """ Episode Comment Schema ."""
    episode_id:int
    comment:str

class CharacterComment(BaseModel):
    """ Character Comment Schema ."""
    character_id:int
    comment:str

class CommentUpdate(BaseModel):
    """ Comment Update Schema ."""
    comment:str

class CommentSchemaType(CommentBase):
    """ Comment Schema ."""
    id: int
    type:CommentType
    status:StatusType

    class Config:
        """ Config schema ."""
        orm_mode = True
