from engine.neighbor_finder import NeighborFinder

from repositories.weight_repository import WeightRepository
from estimators.estimator_strategy import EstimatorStrategy

from estimators.nearest_neighbor_strategy import (
    NearestNeighborStrategy
)


class WeightEstimator:

    def __init__(
        self,
        repository: WeightRepository,
        strategy: EstimatorStrategy | None = None
    ):

        self.repository = repository

        self.strategy = (

            strategy

            or

            NearestNeighborStrategy(
                NeighborFinder()
            )

        )

    def resolver(
        self,
        categoria,
        valor
    ):

        peso = self.repository.buscar_peso(
            categoria,
            valor
        )

        if peso.existe:
            return peso

        return self.strategy.estimar(

            self.repository,

            categoria,

            valor

        )