import aiohttp
from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse, JSONResponse

from berry_app.repository.pokeapi_repo import PokeApiRepo
from berry_app.use_cases.berry_stats import get_berry_statistics

router = APIRouter()


@router.get('/', response_class=HTMLResponse)
async def berry_stats(request: Request):
    async with aiohttp.ClientSession() as session:
        pokeapi_repo = PokeApiRepo(session)
        berry_statistics = await get_berry_statistics(pokeapi_repo)
        return berry_statistics.plot_histogram_html()


@router.get('/allBerryStats', response_class=JSONResponse)
async def get_all_berry_stats():
    async with aiohttp.ClientSession() as session:
        pokeapi_repo = PokeApiRepo(session)
        berry_statistics = await get_berry_statistics(pokeapi_repo)
        return berry_statistics
