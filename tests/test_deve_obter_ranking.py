from benchmarks.benchmark_ranking import BenchmarkRanking

from benchmarks.benchmark_leaderboard import BenchmarkLeaderboard

def test_deve_obter_ranking():

    leaderboard = BenchmarkLeaderboard({

        "rmse": BenchmarkRanking([])

    })

    ranking = leaderboard.obter("rmse")

    assert isinstance(
        ranking,
        BenchmarkRanking
    )