from engine.neighbor_finder import NeighborFinder

from estimators.nearest_neighbor_strategy import (
    NearestNeighborStrategy
)


class WeightEstimator:

    def __init__(
        self,
        repository,
        strategy=None
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