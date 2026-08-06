from engine.neighbor_finder import NeighborFinder
from estimators.nearest_neighbor_strategy import (
    NearestNeighborStrategy
)

from estimators.weight_estimator import WeightEstimator

from tests.fake_weight_repository import (
    FakeWeightRepository
)

import inspect
from estimators.weight_estimator import WeightEstimator

print(inspect.getfile(WeightEstimator))

def test_deve_usar_nearest_neighbor():

    repo = FakeWeightRepository()

    estimator = WeightEstimator(

        repo,

        strategy=NearestNeighborStrategy(

            NeighborFinder()

        )

    )

    peso = estimator.resolver(

        "Pares",

        15

    )

    assert peso.nota == 80