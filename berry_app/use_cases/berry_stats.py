import asyncio
from typing import List

from berry_app.domain.berries import Berry
from berry_app.domain.stats import BerryStatistics
from berry_app.repository.pokeapi_repo import PokeApiRepo


async def get_berry_statistics(
        pokeapi_repo: PokeApiRepo
) -> BerryStatistics:
    berry_ls: List[Berry] = list()
    async for berry_result_item_ls in pokeapi_repo.list_all_berries():
        temp_berry_ls = await asyncio.gather(*(
            pokeapi_repo.get_berry_by_name(berry_result_item.name)
            for berry_result_item in berry_result_item_ls
        ))
        berry_ls.extend(temp_berry_ls)

    return BerryStatistics.get_instance(berry_ls=berry_ls)
