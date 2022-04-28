
""" configuration file."""

from pydantic import BaseSettings

class Settings(BaseSettings):
    """ Settings class."""
    SQLALCHEMY_DB_URL:str
    SECRET_KEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        """ Set Env File Path"""
        env_file = ".env"
