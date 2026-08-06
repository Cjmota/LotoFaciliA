from dataclasses import dataclass, field
from benchmarks.ranking_points_strategy import RankingPointsStrategy
from benchmarks.benchmark_leaderboard import BenchmarkLeaderboard
from benchmarks.benchmark_table import BenchmarkTable
from benchmarks.benchmark_standing import BenchmarkStanding
from benchmarks.benchmark_score import BenchmarkScore
from benchmarks.linear_points_strategy import LinearPointsStrategy


@dataclass(slots=True)
class BenchmarkLeague:

    leaderboard: BenchmarkLeaderboard
    
    estrategia: RankingPointsStrategy = field(
        default_factory=LinearPointsStrategy
    )
    
    def _obter_standing(
        self,
        classificacao: dict[str, BenchmarkStanding],
        estrategia: str
    ) -> BenchmarkStanding:
        
        return classificacao.setdefault(

            estrategia,

            BenchmarkStanding(

                estrategia=estrategia,

                pontos=0

            )

        )
    
    def _registrar_resultado(
        self,
        standing: BenchmarkStanding,
        score: BenchmarkScore,
        total: int
    ) -> None:
        
        pontos = self.estrategia.pontos(
            score.posicao,
            total
        )

        standing.pontos += pontos
        standing.participacoes += 1

        if score.posicao == 1:
            standing.vitorias += 1

        elif score.posicao == 2:
            standing.segundos += 1

        elif score.posicao == 3:
            standing.terceiros += 1

        print(
            standing.estrategia,
            standing.vitorias,
            standing.segundos,
            standing.terceiros,
            standing.pontos
        )
        
    def calcular(self) -> BenchmarkTable:

        classificacao: dict[str, BenchmarkStanding] = {}

        for _, ranking in self.leaderboard:

            total = len(ranking)

            for score in ranking:

                standing = self._obter_standing(
                    classificacao,
                    score.estrategia
                )

                self._registrar_resultado(
                    standing,
                    score,
                    total
                )


        standings = list(classificacao.values())

        return BenchmarkTable(standings)
    