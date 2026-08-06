from benchmarks.benchmark_ranking import BenchmarkRanking
from benchmarks.benchmark_score import BenchmarkScore


def test_deve_atribuir_posicoes():

    ranking = BenchmarkRanking([

        BenchmarkScore(
            estrategia="Bayes",
            atributo="rmse",
            metrica="media",
            valor=0.10
        ),

        BenchmarkScore(
            estrategia="Markov",
            atributo="rmse",
            metrica="media",
            valor=0.20
        ),

        BenchmarkScore(
            estrategia="IA",
            atributo="rmse",
            metrica="media",
            valor=0.30
        ),

    ])

    assert ranking[0].posicao == 1

    assert ranking[1].posicao == 2

    assert ranking[2].posicao == 3