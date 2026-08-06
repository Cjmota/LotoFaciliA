from benchmarks.benchmark_score import BenchmarkScore

def test_deve_permitir_atualizar_posicao():

    score = BenchmarkScore(

        estrategia="Bayes",

        atributo="rmse",

        metrica="media",

        valor=0.10

    )

    score.posicao = 1

    assert score.posicao == 1