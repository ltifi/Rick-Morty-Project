from fastapi import APIRouter

from routes import character as characterApi
from routes import episode as episodeApi
from routes import comment as commentApi

router = APIRouter()

router.include_router(characterApi.app)
router.include_router(episodeApi.app)
router.include_router(commentApi.app)
