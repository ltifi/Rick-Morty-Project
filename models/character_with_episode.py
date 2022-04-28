""" Character in episode model."""

from sqlalchemy import Column, Integer, String, ForeignKey, Table, Text
from sqlalchemy.orm import relationship
from config.database import engine, Base

EpisodeCharacterRelation = Table('episodeCharacterRelation', Base.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('character_id', Integer, ForeignKey('characters.id')),
    Column('episode_id', Integer, ForeignKey('episodes.id'))
)

class Character(Base):
    """ Character model."""
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(115), unique=False, index=False, nullable=True)
    status = Column(String(115), unique=False, index=True)
    species = Column(String(115), unique=False, index=False, nullable=True)
    type = Column(String(200), unique=False, index=False, nullable=True)
    gender = Column(String(115), unique=False, index=False, nullable=True)
    episodes = relationship("Episode",
                    secondary=EpisodeCharacterRelation,
                    back_populates="characters")



class Episode(Base):
    """ Episode model."""
    __tablename__ = "episodes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(115), unique=False, index=False, nullable=True)
    air_date = Column(String(115), unique=False, index=True)
    episode= Column(String(32), unique=False, index=False, nullable=True)
    description=Column(Text, unique=False, index=False, nullable=True)
    characters = relationship("Character",
                    secondary=EpisodeCharacterRelation,
                    back_populates="episodes")
Base.metadata.create_all(engine)
