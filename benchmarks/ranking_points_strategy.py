from abc import ABC, abstractmethod


class RankingPointsStrategy(ABC):

    @abstractmethod
    def pontos(
        self,
        posicao: int,
        total: int
    ) -> int:
        pass