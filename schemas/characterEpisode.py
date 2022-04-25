from pydantic import BaseModel
from sqlalchemy.orm import mapper

class episodeCharacterRelationCreate(BaseModel):
    character_id: int
    episode_id : int