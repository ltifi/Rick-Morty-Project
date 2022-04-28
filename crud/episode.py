""" Episode crud file."""

from sqlalchemy.orm import Session
from schemas.episode_schema import EpisodeCreate
from models.character_with_episode import Episode

def create_episode(session: Session, ep_data: EpisodeCreate):
    """ Create new episode row."""
    db_episode_info=Episode(id=ep_data.id,name=ep_data.name,
    air_date=ep_data.air_date,episode=ep_data.episode)
    session.add(db_episode_info)
    session.commit()
    session.refresh(db_episode_info)
    return db_episode_info

def add_description_episode(session: Session, title:str,description:str):
    """ add description for a specific episode row."""
    episode_info  = session.query(Episode).filter(Episode.name== title).scalar()
    if episode_info:
        episode_info.description=description
        session.commit()
        session.refresh(episode_info)
