from benchmarks.linear_points_strategy import LinearPointsStrategy


def test_deve_calcular_pontos_lineares():

    estrategia = LinearPointsStrategy()

    assert estrategia.pontos(1, 5) == 5

    assert estrategia.pontos(2, 5) == 4

    assert estrategia.pontos(3, 5) == 3

    assert estrategia.pontos(4, 5) == 2

    assert estrategia.pontos(5, 5) == 1