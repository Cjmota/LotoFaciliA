from benchmarks.ranking_points_strategy import RankingPointsStrategy

class LinearPointsStrategy(RankingPointsStrategy):

    def pontos(
        self,
        posicao: int,
        total: int
    ) -> int:

        return total - posicao + 1