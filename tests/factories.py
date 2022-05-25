import factory
from factory.fuzzy import FuzzyInteger, FuzzyText

from berry_app.domain.berries import Berry


class BerryFactory(factory.Factory):
    class Meta:
        model = Berry

    id = FuzzyInteger(0, 100)
    name = FuzzyText()
    growth_time = FuzzyInteger(0, 20)
    max_harvest = FuzzyInteger(0, 20)
    natural_gift_power = FuzzyInteger(0, 20)
    size = FuzzyInteger(0, 20)
    smoothness = FuzzyInteger(0, 20)
    soil_dryness = FuzzyInteger(0, 20)
    firmness = {}
    flavors = []
    item = {}
    natural_gift_type = {}
