from sqlalchemy.orm import Session
from schemas.episode import EpisodeCreate
from models.characterWithEpisode import Episode

def create_episode(db: Session, ep_data: EpisodeCreate):
    db_Episode=Episode(id=ep_data.id,name=ep_data.name,air_date=ep_data.air_date,episode=ep_data.episode)
    db.add(db_Episode)
    db.commit()
    db.refresh(db_Episode)
    return db_Episode

def add_description_episode(db: Session, title:str,description:str):
    episode_info  = db.query(Episode).filter(Episode.name== title).scalar()
    if episode_info:
        episode_info.description=description
        db.commit()
        db.refresh(episode_info)