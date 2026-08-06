from benchmarks.benchmark_league import BenchmarkLeague

from tests.builders.benchmark_leaderboard_builder import (
    BenchmarkLeaderboardBuilder,
)

from tests.fakes.strategies import empate_por_pontos


def test_deve_desempatar_por_vitorias():

    leaderboard = (

        BenchmarkLeaderboardBuilder()

            .ranking(
                "rmse",
                ["Bayes", "Markov", "IA"]
            )

            .ranking(
                "mae",
                ["Bayes", "IA", "Markov"]
            )

            .ranking(
                "mape",
                ["Markov", "IA", "Bayes"]
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
        "Markov",
        "IA"
    ]