from datetime import date

from domain.concurso import Concurso


def test_deve_criar_concurso():

    concurso = Concurso(

        numero=1,

        data=date(2026, 1, 1),

        dezenas=frozenset({

            1, 2, 3, 4, 5,

            6, 7, 8, 9, 10,

            11, 12, 13, 14, 15

        })

    )

    assert concurso.numero == 1

    assert concurso.data == date(2026, 1, 1)

    assert len(concurso.dezenas) == 15

def test_deve_conter_dezena():

    concurso = Concurso(

        numero=1,

        data=date(2026, 1, 1),

        dezenas=frozenset({

            1, 2, 3, 4, 5,
            6, 7, 8, 9, 10,
            11, 12, 13, 14, 15

        })

    )

    assert concurso.contem(10)

    assert not concurso.contem(25)

def test_deve_calcular_soma():

    concurso = Concurso(

        numero=1,

        data=date(2026, 1, 1),

        dezenas=frozenset({

            1, 2, 3, 4, 5,
            6, 7, 8, 9, 10,
            11, 12, 13, 14, 15

        })

    )

    assert concurso.soma() == 120
    
def test_deve_calcular_pares():

    concurso = Concurso(

        numero=1,

        data=date(2026, 1, 1),

        dezenas=frozenset({

            1, 2, 3, 4, 5,
            6, 7, 8, 9, 10,
            11, 12, 13, 14, 15

        })

    )

    assert concurso.pares() == 7
    
def test_deve_calcular_impares():

    concurso = Concurso(

        numero=1,

        data=date(2026, 1, 1),

        dezenas=frozenset({

            1, 2, 3, 4, 5,
            6, 7, 8, 9, 10,
            11, 12, 13, 14, 15

        })

    )

    assert concurso.impares() == 8
    
def test_deve_calcular_acertos():

    concurso = Concurso(

        numero=1,

        data=date(2026, 1, 1),

        dezenas=frozenset({

            1,2,3,4,5,
            6,7,8,9,10,
            11,12,13,14,15

        })

    )

    jogo = frozenset({

        1,2,3,4,5,
        16,17,18,19,20,
        21,22,23,24,25

    })

    assert concurso.acertos(jogo) == 5
    
def test_deve_calcular_linhas():

    concurso = Concurso(

        numero=1,

        data=date(2026, 1, 1),

        dezenas=frozenset({

            1,2,3,4,5,
            6,7,8,9,10,
            11,12,13,14,15

        })

    )

    assert concurso.linhas() == (
        5,
        5,
        5,
        0,
        0
    )

def test_deve_calcular_colunas():

    concurso = Concurso(

        numero=1,

        data=date(2026, 1, 1),

        dezenas=frozenset({

            1,2,3,4,5,
            6,7,8,9,10,
            11,12,13,14,15

        })

    )

    assert concurso.colunas() == (
        3,
        3,
        3,
        3,
        3
    )
    
def test_deve_calcular_consecutivos():

    concurso = Concurso(

        numero=1,

        data=date(2026, 1, 1),

        dezenas=frozenset({

            1, 2, 3,
            5,
            7, 8,
            10,
            12, 13,
            15,
            18,
            20,
            22,
            24, 25

        })

    )

    assert concurso.consecutivos() == 5

    