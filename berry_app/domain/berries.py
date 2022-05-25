import dataclasses
from typing import Any, List


@dataclasses.dataclass
class Berry(object):
    id: int
    name: str
    growth_time: int
    max_harvest: int
    natural_gift_power: int
    size: int
    smoothness: int
    soil_dryness: int
    firmness: Any
    flavors: List
    item: Any
    natural_gift_type: Any

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
