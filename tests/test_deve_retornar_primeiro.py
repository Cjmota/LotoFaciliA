from benchmarks.benchmark_ranking import BenchmarkRanking

from benchmarks.benchmark_score import BenchmarkScore

def test_deve_retornar_primeiro():

    ranking = BenchmarkRanking([

        BenchmarkScore("Bayes", "rmse", "media", 0.10),

        BenchmarkScore("Markov", "rmse", "media", 0.20),

    ])

    assert ranking.primeiro().estrategia == "Bayes"