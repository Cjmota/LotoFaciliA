from benchmarks.benchmark_ranking import BenchmarkRanking

from benchmarks.benchmark_leaderboard import BenchmarkLeaderboard

from benchmarks.benchmark_score import BenchmarkScore

from benchmarks.benchmark_league import BenchmarkLeague

from benchmarks.linear_points_strategy import LinearPointsStrategy

def test_deve_contabilizar_participacoes():

    ranking_rmse = BenchmarkRanking([

        BenchmarkScore("Bayes", "rmse", "media", 0.10),

        BenchmarkScore("Markov", "rmse", "media", 0.20),

        BenchmarkScore("IA", "rmse", "media", 0.30),

    ])

    ranking_mae = BenchmarkRanking([

        BenchmarkScore("Bayes", "mae", "media", 0.05),

        BenchmarkScore("IA", "mae", "media", 0.08),

        BenchmarkScore("Markov", "mae", "media", 0.09),

    ])

    leaderboard = BenchmarkLeaderboard({

        "rmse": ranking_rmse,

        "mae": ranking_mae

    })

    league = BenchmarkLeague(

        leaderboard,

        LinearPointsStrategy()

    )

    tabela = league.calcular()

    assert tabela.obter("Bayes").participacoes == 2

    assert tabela.obter("Markov").participacoes == 2

    assert tabela.obter("IA").participacoes == 2