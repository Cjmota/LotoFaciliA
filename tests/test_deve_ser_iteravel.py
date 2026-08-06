from benchmarks.benchmark_leaderboard import BenchmarkLeaderboard
from benchmarks.benchmark_ranking import BenchmarkRanking


def test_deve_ser_iteravel():

    leaderboard = BenchmarkLeaderboard({

        "rmse": BenchmarkRanking([]),

        "mae": BenchmarkRanking([])

    })

    assert [

        metrica

        for metrica, _ in leaderboard

    ] == [

        "rmse",

        "mae"

    ]