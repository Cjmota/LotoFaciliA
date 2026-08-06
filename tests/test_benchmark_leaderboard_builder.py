from tests.builders.benchmark_leaderboard_builder import (
    BenchmarkLeaderboardBuilder
)


def test_deve_construir_leaderboard():

    leaderboard = (

        BenchmarkLeaderboardBuilder()

            .ranking(
                "rmse",
                ["Bayes", "Markov", "IA"]
            )

            .ranking(
                "mae",
                ["IA", "Bayes", "Markov"]
            )

            .build()

    )

    assert "rmse" in leaderboard

    assert "mae" in leaderboard

    assert len(leaderboard) == 2