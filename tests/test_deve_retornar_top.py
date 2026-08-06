from benchmarks.benchmark_ranking import BenchmarkRanking
from benchmarks.benchmark_score import BenchmarkScore


def test_deve_retornar_top():

    ranking = BenchmarkRanking([

        BenchmarkScore("Bayes", "rmse", "media", 0.10),

        BenchmarkScore("Markov", "rmse", "media", 0.20),

        BenchmarkScore("IA", "rmse", "media", 0.30),

    ])

    top = ranking.top(2)

    assert len(top) == 2

    assert top.primeiro().estrategia == "Bayes"

    assert top.ultimo().estrategia == "Markov"