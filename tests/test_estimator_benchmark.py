from benchmarks.estimator_benchmark import EstimatorBenchmark

from engine.neighbor_finder import NeighborFinder

from estimators.nearest_neighbor_strategy import (
    NearestNeighborStrategy
)

from estimators.weight_estimator import WeightEstimator

from tests.fake_weight_repository import (
    FakeWeightRepository
)


def test_benchmark_deve_avaliar_todos_os_valores():

    repo = FakeWeightRepository()

    estimator = WeightEstimator(
        repo,
        strategy=NearestNeighborStrategy(
            NeighborFinder()
        )
    )

    benchmark = EstimatorBenchmark(repo)

    resultados = benchmark.avaliar(
        estimator,
        "Pares"
    )

    assert len(resultados) == len(
        repo.valores("Pares")
    )

    resultado = resultados[0]

    assert resultado.categoria == "Pares"
    assert resultado.valor == 10

    assert resultado.real.existe
    assert resultado.estimado.existe