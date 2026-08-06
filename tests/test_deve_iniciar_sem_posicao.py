from benchmarks.benchmark_score import BenchmarkScore

def test_deve_iniciar_sem_posicao():

    score = BenchmarkScore(

        estrategia="Bayes",

        atributo="rmse",

        metrica="media",

        valor=0.10

    )

    assert score.posicao is None