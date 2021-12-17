from mcstatus import MinecraftServer
from servers_stats_microservice.api.models import ServerStats, Players


async def get_stats(ip: str, port: int = 25565) -> ServerStats:
    server = MinecraftServer(ip, port)
    status = await server.async_status()
    query = await server.async_query()

    return ServerStats(
        ip=ip,
        port=port,
        description=status.description,
        version=status.version.name,
        latency=status.latency,
        players=Players(
            online=query.players.online,
            max=query.players.max,
            list=query.players.names,
        ),
    )
