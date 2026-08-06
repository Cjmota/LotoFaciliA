from benchmarks.benchmark_ranking import BenchmarkRanking
from benchmarks.benchmark_score import BenchmarkScore


def test_deve_retornar_bottom():

    ranking = BenchmarkRanking([

        BenchmarkScore("Bayes", "rmse", "media", 0.10),

        BenchmarkScore("Markov", "rmse", "media", 0.20),

        BenchmarkScore("IA", "rmse", "media", 0.30),

    ])

    bottom = ranking.bottom(2)

    assert len(bottom) == 2

    assert bottom.primeiro().estrategia == "Markov"

    assert bottom.ultimo().estrategia == "IA"
    
    