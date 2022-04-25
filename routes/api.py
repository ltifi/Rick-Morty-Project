from fastapi import APIRouter

from routes import character as characterApi
from routes import episode as episodeApi

router = APIRouter()

router.include_router(characterApi.app)
router.include_router(episodeApi.app)