from benchmarks.benchmark_ranking import BenchmarkRanking

from benchmarks.benchmark_leaderboard import BenchmarkLeaderboard


def test_deve_iterar_rankings():

    leaderboard = BenchmarkLeaderboard({

        "rmse": BenchmarkRanking([]),

        "mae": BenchmarkRanking([])

    })

    assert len(list(leaderboard)) == 2