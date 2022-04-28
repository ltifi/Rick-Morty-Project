""" database configuration file."""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from config import config

# Make the engine
engine = create_engine(config.Settings().SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Make the DeclarativeMeta
Base = declarative_base()
