from benchmarks.benchmark_score import BenchmarkScore


def test_deve_criar_score():

    score = BenchmarkScore(
        estrategia="Bayes",
        atributo="rmse",
        metrica="media",
        valor=0.10
    )

    assert score.estrategia == "Bayes"
    assert score.atributo == "rmse"
    assert score.metrica == "media"
    assert score.valor == 0.10


def test_deve_iniciar_sem_posicao():

    score = BenchmarkScore(
        estrategia="Bayes",
        atributo="rmse",
        metrica="media",
        valor=0.10
    )

    assert score.posicao is None


def test_deve_permitir_atualizar_posicao():

    score = BenchmarkScore(
        estrategia="Bayes",
        atributo="rmse",
        metrica="media",
        valor=0.10
    )

    score.posicao = 1

    assert score.posicao == 1

