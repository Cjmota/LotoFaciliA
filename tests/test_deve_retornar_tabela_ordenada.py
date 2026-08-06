from benchmarks.benchmark_league import BenchmarkLeague
from benchmarks.benchmark_leaderboard import BenchmarkLeaderboard
from benchmarks.benchmark_ranking import BenchmarkRanking
from benchmarks.benchmark_score import BenchmarkScore
from benchmarks.linear_points_strategy import LinearPointsStrategy


def test_deve_retornar_tabela_ordenada():

    ranking_rmse = BenchmarkRanking([

        BenchmarkScore("Bayes", "rmse", "media", 0.10),

        BenchmarkScore("Markov", "rmse", "media", 0.20),

        BenchmarkScore("IA", "rmse", "media", 0.30),

    ])

    leaderboard = BenchmarkLeaderboard({

        "rmse": ranking_rmse

    })

    league = BenchmarkLeague(

        leaderboard,

        LinearPointsStrategy()

    )

    tabela = league.calcular()

    assert tabela.classificacao[0].estrategia == "Bayes"

    assert tabela.classificacao[1].estrategia == "Markov"

    assert tabela.classificacao[2].estrategia == "IA"