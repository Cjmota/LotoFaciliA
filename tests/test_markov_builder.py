from datetime import date

from analysis.markov_builder import MarkovBuilder
from domain.concurso import Concurso
from domain.historico import Historico


def test_deve_construir_cadeia_de_somas():

    historico = Historico([

        Concurso(
            numero=1,
            data=date(2026,1,1),
            dezenas=frozenset(range(1,16))
        ),

        Concurso(
            numero=2,
            data=date(2026,1,2),
            dezenas=frozenset(range(2,17))
        ),

        Concurso(
            numero=3,
            data=date(2026,1,3),
            dezenas=frozenset(range(3,18))
        )

    ])

    builder = MarkovBuilder()

    cadeia = builder.construir_somas(

        historico

    )

    assert cadeia.probabilidade(

        120,

        135

    ) == 1.0
