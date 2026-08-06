

from benchmarks.ranking_points_strategy import RankingPointsStrategy


class FixedPointsStrategy(RankingPointsStrategy):

    def __init__(self, pontos_por_posicao: dict[int, int]):

        self._pontos_por_posicao = pontos_por_posicao

    def pontos(
        self,
        posicao: int,
        total: int
    ) -> int:

        return self._pontos_por_posicao[posicao]