from tests.fakes.fixed_points_strategy import FixedPointsStrategy


def empate_por_pontos() -> FixedPointsStrategy:
    """
    Estratégia de pontuação utilizada para criar empates
    e testar critérios de desempate da BenchmarkLeague.

    1º = 10 pontos
    2º = 10 pontos
    3º = 0 pontos
    """

    return FixedPointsStrategy({

        1: 10,
        2: 10,
        3: 0

    })