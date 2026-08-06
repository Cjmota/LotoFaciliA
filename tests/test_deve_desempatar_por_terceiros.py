from benchmarks.benchmark_league import BenchmarkLeague

from tests.builders.benchmark_leaderboard_builder import (
    BenchmarkLeaderboardBuilder,
)

from tests.fakes.strategies import empate_por_pontos


def test_deve_desempatar_por_terceiros():

    leaderboard = (

        BenchmarkLeaderboardBuilder()

            .ranking(
                "rmse",
                ["IA", "Markov", "Bayes"]
            )

            .ranking(
                "mae",
                ["Markov", "Bayes", "IA"]
            )

            .ranking(
                "mape",
                ["Bayes", "IA", "Markov"]
            )

            .build()

    )

    league = BenchmarkLeague(
        leaderboard,
        empate_por_pontos()
    )

    tabela = league.calcular()

    assert [
        standing.estrategia
        for standing in tabela
    ] == [
        "Bayes",
        "IA",
        "Markov"
    ]