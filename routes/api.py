""" Regroupe API's."""

from fastapi import APIRouter
from routes import character as characterApi
from routes import episode as episodeApi
from routes import comment as commentApi
from routes import user as userApi
from routes import statistics as statisticApi


router = APIRouter()

router.include_router(characterApi.app)
router.include_router(episodeApi.app)
router.include_router(commentApi.app)
router.include_router(userApi.app)
router.include_router(statisticApi.app)

