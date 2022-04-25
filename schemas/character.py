from typing import List
from pydantic import BaseModel
from schemas.episode import episode

class CharacterBase(BaseModel):
    name : str
    status : str
    species : str
    type : str
    gender : str

class CharacterCreate(CharacterBase):
    episode_ids: List[int] = []

class character(CharacterBase):
    episodes: List[episode] = []

    class Config:
        orm_mode = True
