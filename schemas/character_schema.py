""" Character Schema ."""

from typing import List
from pydantic import BaseModel
from schemas.episode_schema import EpisodeBase

class CharacterBase(BaseModel):
    """ Character Base Schema ."""
    name : str
    status : str
    species : str
    type : str
    gender : str

class CharacterCreate(CharacterBase):
    """ Character Create Schema ."""
    episode_ids: List[int] = []

class Character(CharacterBase):
    """ Character Schema ."""
    episodes: List[EpisodeBase] = []

    class Config:
        orm_mode = True
