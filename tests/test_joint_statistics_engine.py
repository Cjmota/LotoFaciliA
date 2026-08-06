from engine.joint_statistics.joint_statistics_engine import JointStatisticsEngine


class ConcursoFake:

    def __init__(

        self,

        pares,

        primos

    ):

        self.pares = pares
        self.primos = primos


def test_joint_statistics():

    historico = [

        ConcursoFake(7, 5),

        ConcursoFake(7, 5),

        ConcursoFake(8, 5),

        ConcursoFake(8, 4),

        ConcursoFake(8, 4),

        ConcursoFake(8, 4),

    ]

    engine = JointStatisticsEngine(

        historico,

        ("pares", "primos")

    )

    resultado = engine.calcular()

    assert resultado.total == 6

    assert resultado.frequencia((7, 5)) == 2

    assert resultado.frequencia((8, 5)) == 1

    assert resultado.frequencia((8, 4)) == 3

    assert resultado.quantidade_combinacoes == 3