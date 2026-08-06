from benchmarks.benchmark_leaderboard import BenchmarkLeaderboard
from benchmarks.benchmark_ranking import BenchmarkRanking


def test_deve_criar_leaderboard():

    leaderboard = BenchmarkLeaderboard({

        "rmse": BenchmarkRanking([]),

        "mae": BenchmarkRanking([])

    })

    assert len(leaderboard.rankings) == 2