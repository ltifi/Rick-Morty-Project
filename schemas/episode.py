from typing import Optional, List
from pydantic import BaseModel
from sqlalchemy.orm import mapper

class EpisodeBase(BaseModel):
    name: str
    air_date : str
    episode : str
    description : Optional[str] = None

class EpisodeCreate(EpisodeBase):
    character_ids: List[int] = []

class episode(EpisodeBase):
    pass

    class Config:
        orm_mode = True
