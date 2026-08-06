from benchmarks.benchmark_ranking import BenchmarkRanking

from benchmarks.benchmark_leaderboard import BenchmarkLeaderboard

def test_deve_conter_ranking():

    leaderboard = BenchmarkLeaderboard({

        "rmse": BenchmarkRanking([])

    })

    assert "rmse" in leaderboard

    assert "mae" not in leaderboard
