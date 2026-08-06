from engine.neighbor_finder import NeighborFinder
from engine.weight_interpolator import WeightInterpolator

from estimators.interpolation_strategy import InterpolationStrategy

from tests.fake_weight_repository import FakeWeightRepository


def test_deve_retornar_peso_existente_quando_valor_for_igual_ao_inferior():

    repository = FakeWeightRepository()

    strategy = InterpolationStrategy(
        NeighborFinder(),
        WeightInterpolator()
    )

    resultado = strategy.estimar(
        repository,
        "Pares",
        10
    )

    assert resultado.nota == 80