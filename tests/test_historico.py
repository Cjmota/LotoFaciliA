from datetime import date

from domain.concurso import Concurso
from domain.historico import Historico


def test_deve_criar_historico():

    concurso = Concurso(

        numero=1,

        data=date(2026, 1, 1),

        dezenas=frozenset({

            1, 2, 3, 4, 5,
            6, 7, 8, 9, 10,
            11, 12, 13, 14, 15

        })

    )

    historico = Historico([

        concurso

    ])

    assert len(historico) == 1

def test_deve_ser_iteravel():

    concurso1 = Concurso(

        numero=1,

        data=date(2026, 1, 1),

        dezenas=frozenset(range(1, 16))

    )

    concurso2 = Concurso(

        numero=2,

        data=date(2026, 1, 2),

        dezenas=frozenset(range(11, 26))

    )

    historico = Historico([

        concurso1,

        concurso2

    ])

    assert [

        concurso.numero

        for concurso in historico

    ] == [

        1,

        2

    ]
    
def test_deve_retornar_primeiro():

    concurso1 = Concurso(
        numero=1,
        data=date(2026, 1, 1),
        dezenas=frozenset(range(1, 16))
    )

    concurso2 = Concurso(
        numero=2,
        data=date(2026, 1, 2),
        dezenas=frozenset(range(11, 26))
    )

    historico = Historico([
        concurso1,
        concurso2
    ])

    assert historico.primeiro().numero == 1

def test_deve_retornar_ultimo():

    concurso1 = Concurso(
        numero=1,
        data=date(2026, 1, 1),
        dezenas=frozenset(range(1, 16))
    )

    concurso2 = Concurso(
        numero=2,
        data=date(2026, 1, 2),
        dezenas=frozenset(range(11, 26))
    )

    historico = Historico([
        concurso1,
        concurso2
    ])

    assert historico.ultimo().numero == 2

def test_deve_obter_concurso():

    concurso1 = Concurso(
        numero=1,
        data=date(2026, 1, 1),
        dezenas=frozenset(range(1, 16))
    )

    concurso2 = Concurso(
        numero=2,
        data=date(2026, 1, 2),
        dezenas=frozenset(range(11, 26))
    )

    historico = Historico([
        concurso1,
        concurso2
    ])

    concurso = historico.obter(2)

    assert concurso.numero == 2

def test_deve_conter_concurso():

    concurso1 = Concurso(
        numero=1,
        data=date(2026, 1, 1),
        dezenas=frozenset(range(1, 16))
    )

    historico = Historico([
        concurso1
    ])

    assert 1 in historico

    assert 2 not in historico

