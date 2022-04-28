""" Character in episode Schema ."""

from pydantic import BaseModel

class EpisodeCharacterRelationCreate(BaseModel):
    """ Character in episode Class ."""
    character_id: int
    episode_id : int
