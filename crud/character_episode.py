""" Character in episode crud file."""

from sqlalchemy.orm import Session
from schemas.character_episode_schema import EpisodeCharacterRelationCreate
from models.character_with_episode import EpisodeCharacterRelation

def create_episode_character_relation(session: Session,epchr_data: EpisodeCharacterRelationCreate):
    """ Create new characetr in episode row."""
    statement = EpisodeCharacterRelation.insert().values(character_id=epchr_data.character_id,
     episode_id=epchr_data.episode_id)
    session.execute(statement)
    session.commit()
    return epchr_data
