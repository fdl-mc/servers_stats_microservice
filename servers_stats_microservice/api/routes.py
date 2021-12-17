from fastapi.routing import APIRouter
from servers_stats_microservice.api.models import ServerStats
from servers_stats_microservice.api.utils import get_stats


stats = APIRouter()


@stats.get("/main", response_model=ServerStats)
async def main_stats():
    return await get_stats("play.fdl-mc.ru")


@stats.get("/creative", response_model=ServerStats)
async def creative_stats():
    return await get_stats("creative.fdl-mc.ru")
