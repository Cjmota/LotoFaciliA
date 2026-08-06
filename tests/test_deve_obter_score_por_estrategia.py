from benchmarks.benchmark_ranking import BenchmarkRanking

from benchmarks.benchmark_score import BenchmarkScore

def test_deve_obter_score_por_estrategia():

    ranking = BenchmarkRanking([

        BenchmarkScore(
            estrategia="Bayes",
            atributo="nota",
            metrica="rmse",
            valor=1
        ),

        BenchmarkScore(
            estrategia="Markov",
            atributo="nota",
            metrica="rmse",
            valor=2
        )

    ])

    score = ranking.obter("Bayes")

    assert score.estrategia == "Bayes"

    assert score.valor == 1