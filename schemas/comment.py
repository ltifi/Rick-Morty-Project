from typing import Optional
from pydantic import BaseModel
from sqlalchemy.orm import mapper
from models.enums import StatusType, CommentType
from models.characterWithEpisode import EpisodeCharacterRelation

class CommentBase(BaseModel):
    character_id: Optional[int] = None
    episode_id : Optional[int] = None
    type : CommentType = "character_in_episode"
    comment : str
    status : StatusType = "Review"
    
class EpisodeComment(BaseModel):
    episode_id:int
    comment:str
    type:CommentType
    status:StatusType = "Review"

class CharacterComment(BaseModel):
    character_id:int
    comment:str
    type:CommentType = "Character"
    status:StatusType = "Review"

class CommentUpdate(BaseModel):
    comment:str

class comment(CommentBase):
    id: int

    class Config:
        orm_mode = True