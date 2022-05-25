import dataclasses
from typing import Optional, List


@dataclasses.dataclass
class ResultItem:
    name: str
    url: str

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


@dataclasses.dataclass
class Page:
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[ResultItem]

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
