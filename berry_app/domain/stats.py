import collections
import dataclasses
import statistics
from typing import List, Dict

import matplotlib.pyplot as plot
import mpld3

from berry_app.domain.berries import Berry


@dataclasses.dataclass
class BerryStatistics:
    berries_names: List[str]
    min_growth_time: int
    max_growth_time: int
    mean_growth_time: float
    median_growth_time: float
    variance_growth_time: float
    frequency_growth_time: Dict

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)

    @classmethod
    def get_instance(cls, berry_ls: List[Berry]):
        growth_time_ls, berry_name_ls = [], []

        # Use classic for instead of map for performance reasons
        for berry in berry_ls:
            berry_name_ls.append(berry.name)
            growth_time_ls.append(berry.growth_time)

        return cls(
            berries_names=berry_name_ls,
            min_growth_time=min(growth_time_ls),
            max_growth_time=max(growth_time_ls),
            mean_growth_time=statistics.mean(growth_time_ls),
            median_growth_time=statistics.median(growth_time_ls),
            variance_growth_time=statistics.variance(growth_time_ls),
            frequency_growth_time=dict(collections.Counter(growth_time_ls))
        )

    def plot_histogram_html(self):
        plot_figure = plot.figure()
        plot.bar(self.frequency_growth_time.keys(), self.frequency_growth_time.values())
        plot.title('Growth Time Histogram')
        plot.xlabel('Growth Time')
        plot.ylabel('Frequency')
        plot.plot()
        return mpld3.fig_to_html(plot_figure)

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
