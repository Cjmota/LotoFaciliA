from benchmarks.linear_points_strategy import LinearPointsStrategy

from benchmarks.benchmark_ranking import BenchmarkRanking

from benchmarks.benchmark_score import BenchmarkScore

from benchmarks.benchmark_leaderboard import BenchmarkLeaderboard

from benchmarks.benchmark_league import BenchmarkLeague

def test_deve_calcular_pontos_da_liga():

    ranking_rmse = BenchmarkRanking([
        BenchmarkScore("Bayes", "rmse", "media", 0.10, 1),
        BenchmarkScore("Markov", "rmse", "media", 0.15, 2),
        BenchmarkScore("IA", "rmse", "media", 0.20, 3),
    ])

    ranking_mae = BenchmarkRanking([
        BenchmarkScore("Markov", "mae", "media", 0.05, 1),
        BenchmarkScore("Bayes", "mae", "media", 0.06, 2),
        BenchmarkScore("IA", "mae", "media", 0.09, 3),
    ])

    leaderboard = BenchmarkLeaderboard({
        "rmse": ranking_rmse,
        "mae": ranking_mae,
    })

    league = BenchmarkLeague(
        leaderboard,
        LinearPointsStrategy()
    )

    tabela = league.calcular()

    assert tabela.obter("Bayes").pontos == 5
    assert tabela.obter("Markov").pontos == 5
    assert tabela.obter("IA").pontos == 2