""" Episode Schema ."""

from typing import Optional, List
from pydantic import BaseModel

class EpisodeBase(BaseModel):
    """ Episode Base Schema ."""
    name: str
    air_date : str
    episode : str
    description : Optional[str] = None

class EpisodeCreate(EpisodeBase):
    """ Episode Create Schema ."""
    character_ids: List[int] = []
