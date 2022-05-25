from unittest import mock

import pytest

from berry_app.domain.pagination import ResultItem
from berry_app.domain.stats import BerryStatistics
from berry_app.use_cases.berry_stats import get_berry_statistics
from tests.factories import BerryFactory


class AsyncIterator:
    def __init__(self, seq):
        self.iter = iter(seq)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            return next(self.iter)
        except StopIteration:
            raise StopAsyncIteration


@pytest.fixture
def domain_berries_result_item():
    berry_result_item_1 = ResultItem(
        name='berry_1',
        url='fake.com/fake/path/1'
    )
    berry_result_item_2 = ResultItem(
        name='berry_2',
        url='fake.com/fake/path/2'
    )
    berry_result_item_3 = ResultItem(
        name='berry_3',
        url='fake.com/fake/path/3/'
    )

    data = [berry_result_item_1, berry_result_item_2, berry_result_item_3]

    return AsyncIterator([(item for item in data)])


@pytest.fixture
def domain_berries(*args, **kwargs):
    berry_1 = BerryFactory(
        id=1,
        name='berry_1',
        growth_time=5
    )
    berry_2 = BerryFactory(
        id=2,
        name='berry_2',
        growth_time=10,
    )
    berry_3 = BerryFactory(
        id=3,
        name='berry_3',
        growth_time=2
    )
    return [berry_1, berry_2, berry_3]


@pytest.mark.anyio
async def test_get_berry_statistics(domain_berries_result_item, domain_berries):
    repo = mock.Mock()
    repo.list_all_berries.return_value = domain_berries_result_item
    repo.get_berry_by_name = mock.AsyncMock()
    repo.get_berry_by_name.side_effect = domain_berries

    result = await get_berry_statistics(repo)
    expected = BerryStatistics(
        berries_names=['berry_1', 'berry_2', 'berry_3'],
        min_growth_time=2,
        max_growth_time=10,
        mean_growth_time=5.666666666666667,
        median_growth_time=5,
        variance_growth_time=16.333333333333332,
        frequency_growth_time={5: 1, 10: 1, 2: 1}
    )
    assert result == expected
