from benchmarks.benchmark_ranking import BenchmarkRanking

from benchmarks.benchmark_leaderboard import BenchmarkLeaderboard

from benchmarks.benchmark_score import BenchmarkScore

from benchmarks.benchmark_league import BenchmarkLeague

from benchmarks.linear_points_strategy import LinearPointsStrategy

from benchmarks.benchmark_table import BenchmarkTable

def test_deve_retornar_benchmark_table():

    ranking_rmse = BenchmarkRanking([

        BenchmarkScore("Bayes", "rmse", "media", 0.10),

        BenchmarkScore("Markov", "rmse", "media", 0.20),

        BenchmarkScore("IA", "rmse", "media", 0.30),

    ])

    ranking_mae = BenchmarkRanking([

        BenchmarkScore("IA", "mae", "media", 0.05),

        BenchmarkScore("Bayes", "mae", "media", 0.08),

        BenchmarkScore("Markov", "mae", "media", 0.09),

    ])

    leaderboard = BenchmarkLeaderboard({

        "rmse": ranking_rmse,

        "mae": ranking_mae

    })

    campeonato = BenchmarkLeague(
        leaderboard,
        LinearPointsStrategy()
    )

    tabela = campeonato.calcular()

    assert isinstance(tabela, BenchmarkTable)
    
