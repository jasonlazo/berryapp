from typing import Generator, Any

from aiohttp import ClientSession, ClientError
from retry import retry

from berry_app import config
from berry_app.domain.berries import Berry
from berry_app.domain.pagination import Page, ResultItem


class PokeApiRepo:

    def __init__(self, client_session):
        self.session: ClientSession = client_session

    @retry(exceptions=(ClientError,), tries=config.HTTP_RETRIES)
    async def list_all_berries(self) -> Generator[Generator[ResultItem, Any, None], Any, None]:
        url_template = 'https://pokeapi.co/api/v2/berry/?offset={:d}&limit={:d}'
        url = url_template.format(0, config.PAGE_SIZE)
        while url:
            async with self.session.get(url) as response:
                if response.ok:
                    page = Page.from_dict(await response.json())
                    url = page.next
                    yield (ResultItem.from_dict(item) for item in page.results)

    @retry(exceptions=(ClientError,), tries=config.HTTP_RETRIES)
    async def get_berry_by_name(self, name: str) -> Berry:
        url_template = 'https://pokeapi.co/api/v2/berry/{name}/'
        async with self.session.get(url_template.format(name=name)) as response:
            if response.ok:
                return Berry.from_dict(await response.json())
