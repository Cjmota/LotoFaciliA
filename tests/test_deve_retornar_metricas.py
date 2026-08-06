from benchmarks.benchmark_leaderboard import BenchmarkLeaderboard
from benchmarks.benchmark_ranking import BenchmarkRanking


def test_deve_retornar_metricas():

    leaderboard = BenchmarkLeaderboard({

        "rmse": BenchmarkRanking([]),

        "mae": BenchmarkRanking([]),

        "desvio_padrao": BenchmarkRanking([])

    })

    assert leaderboard.metricas == (

        "rmse",

        "mae",

        "desvio_padrao"

    )