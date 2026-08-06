from benchmarks.benchmark_leaderboard import BenchmarkLeaderboard

from benchmarks.benchmark_ranking import BenchmarkRanking

def test_deve_conter_metrica():

    leaderboard = BenchmarkLeaderboard({

        "rmse": BenchmarkRanking([])

    })

    assert "rmse" in leaderboard

    assert "mae" not in leaderboard
    