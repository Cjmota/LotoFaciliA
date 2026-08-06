from benchmarks.benchmark_leaderboard import BenchmarkLeaderboard
from benchmarks.benchmark_ranking import BenchmarkRanking
from benchmarks.benchmark_score import BenchmarkScore


class BenchmarkLeaderboardBuilder:

    def __init__(self):

        self._rankings: dict[str, BenchmarkRanking] = {}


    # O BenchmarkRanking define a posição pela ordem da lista.
    # O valor é apenas um placeholder para os testes.

    def ranking(
        self,
        atributo: str,
        estrategias: list[str],
        metrica: str = "media"
    ) -> "BenchmarkLeaderboardBuilder":

        scores = []

        for indice, estrategia in enumerate(estrategias, start=1):

            scores.append(

                BenchmarkScore(

                    estrategia=estrategia,

                    atributo=atributo,

                    metrica=metrica,

                    valor=float(indice)

                )

            )

        self._rankings[atributo] = BenchmarkRanking(scores)

        return self

    def build(self) -> BenchmarkLeaderboard:

        return BenchmarkLeaderboard(self._rankings)