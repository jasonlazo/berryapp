import unittest
from unittest import mock

from berry_app.domain.pagination import ResultItem
from berry_app.repository.pokeapi_repo import PokeApiRepo
from tests.factories import BerryFactory

berries_page_json = {
    "count": 2,
    "next": None,
    "previous": None,
    "results": [
        {
            "name": "berry_1",
            "url": "https://pokeapi.co/api/v2/berry/1/"
        },
        {
            "name": "berry_2",
            "url": "https://pokeapi.co/api/v2/berry/2/"
        }
    ]
}


class PokeApiRepoTestCase(unittest.IsolatedAsyncioTestCase):

    async def test_list_all_berries(self):
        client_mock = mock.Mock()
        client_mock.get.return_value = ctx_mock = mock.AsyncMock()
        ctx_mock.__aenter__.return_value.ok = True
        ctx_mock.__aenter__.return_value.json.return_value = berries_page_json

        pokeapi_repo = PokeApiRepo(client_mock)
        result = [
            [item for item in berry_result_item_ls]
            async for berry_result_item_ls in pokeapi_repo.list_all_berries()
        ]

        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), 2)

        self.assertEqual(result[0][0], ResultItem(name='berry_1', url='https://pokeapi.co/api/v2/berry/1/'))
        self.assertEqual(result[0][1], ResultItem(name='berry_2', url='https://pokeapi.co/api/v2/berry/2/'))

    async def test_get_berry_by_name(self):
        client_mock = mock.Mock()
        client_mock.get.return_value = ctx_mock = mock.AsyncMock()
        ctx_mock.__aenter__.return_value.ok = True
        expected = BerryFactory()
        ctx_mock.__aenter__.return_value.json.return_value = expected.to_dict()

        pokeapi_repo = PokeApiRepo(client_mock)
        result = await pokeapi_repo.get_berry_by_name(expected.name)
        self.assertEqual(result, expected)
