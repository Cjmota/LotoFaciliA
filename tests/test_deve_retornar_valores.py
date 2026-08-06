from benchmarks.benchmark_ranking import BenchmarkRanking
from benchmarks.benchmark_score import BenchmarkScore


def test_deve_retornar_valores():

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
        ),

        BenchmarkScore(
            estrategia="Interpolação",
            atributo="nota",
            metrica="rmse",
            valor=3
        )

    ])

    assert ranking.valores() == (

        1,

        2,

        3

    )