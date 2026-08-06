from analysis.historico_analyzer import HistoricoAnalyzer
from domain.historico import Historico
from domain.concurso import Concurso
from datetime import date


def test_deve_criar_analyzer():

    historico = Historico([])

    analyzer = HistoricoAnalyzer(historico)

    assert analyzer.historico is historico

def test_deve_calcular_frequencia():

    historico = Historico([

        Concurso(
            numero=1,
            data=date(2026,1,1),
            dezenas=frozenset(range(1,16))
        ),

        Concurso(
            numero=2,
            data=date(2026,1,2),
            dezenas=frozenset({
                1,2,3,
                14,15,
                16,17,18,19,20,
                21,22,23,24,25
            })
        )

    ])

    analyzer = HistoricoAnalyzer(historico)

    assert analyzer.frequencia(1) == 2
    assert analyzer.frequencia(10) == 1
    assert analyzer.frequencia(25) == 1

def test_deve_calcular_frequencias():

    historico = Historico([

        Concurso(
            numero=1,
            data=date(2026,1,1),
            dezenas=frozenset(range(1,16))
        ),

        Concurso(
            numero=2,
            data=date(2026,1,2),
            dezenas=frozenset({
                1,2,3,
                14,15,
                16,17,18,19,20,
                21,22,23,24,25
            })
        )

    ])

    analyzer = HistoricoAnalyzer(historico)

    frequencias = analyzer.frequencias()

    assert frequencias[1] == 2
    assert frequencias[10] == 1
    assert frequencias[14] == 2

def test_deve_calcular_distribuicao_somas():

    historico = Historico([

        Concurso(
            numero=1,
            data=date(2026,1,1),
            dezenas=frozenset(range(1,16))
        ),

        Concurso(
            numero=2,
            data=date(2026,1,2),
            dezenas=frozenset(range(1,16))
        )

    ])

    analyzer = HistoricoAnalyzer(historico)

    distribuicao = analyzer.distribuicao_somas()

    assert distribuicao == {

        120: 2

    }

def test_deve_calcular_distribuicao_pares():

    historico = Historico([

        Concurso(
            numero=1,
            data=date(2026,1,1),
            dezenas=frozenset(range(1,16))
        ),

        Concurso(
            numero=2,
            data=date(2026,1,2),
            dezenas=frozenset(range(11,26))
        )

    ])

    analyzer = HistoricoAnalyzer(historico)

    distribuicao = analyzer.distribuicao_pares()

    assert distribuicao == {

        7: 2

    }

def test_deve_calcular_distribuicao_impares():

    historico = Historico([

        Concurso(
            numero=1,
            data=date(2026,1,1),
            dezenas=frozenset(range(1,16))
        ),

        Concurso(
            numero=2,
            data=date(2026,1,2),
            dezenas=frozenset(range(11,26))
        )

    ])

    analyzer = HistoricoAnalyzer(historico)

    distribuicao = analyzer.distribuicao_impares()

    assert distribuicao == {

        8: 2

    }

def test_deve_calcular_distribuicao_consecutivos():

    historico = Historico([

        Concurso(
            numero=1,
            data=date(2026,1,1),
            dezenas=frozenset(range(1,16))
        ),

        Concurso(
            numero=2,
            data=date(2026,1,2),
            dezenas=frozenset({
                1,2,3,
                5,
                7,8,
                10,
                12,13,
                15,
                18,
                20,
                22,
                24,25
            })
        )

    ])

    analyzer = HistoricoAnalyzer(historico)

    distribuicao = analyzer.distribuicao_consecutivos()

    assert distribuicao == {

        14: 1,
        5: 1

    }

def test_deve_calcular_distribuicao_linhas():

    historico = Historico([

        Concurso(
            numero=1,
            data=date(2026,1,1),
            dezenas=frozenset(range(1,16))
        ),

        Concurso(
            numero=2,
            data=date(2026,1,2),
            dezenas=frozenset(range(11,26))
        )

    ])

    analyzer = HistoricoAnalyzer(historico)

    distribuicao = analyzer.distribuicao_linhas()

    assert distribuicao == {

        (5,5,5,0,0): 1,

        (0,0,5,5,5): 1

    }

def test_deve_calcular_distribuicao_colunas():

    historico = Historico([

        Concurso(
            numero=1,
            data=date(2026,1,1),
            dezenas=frozenset(range(1,16))
        ),

        Concurso(
            numero=2,
            data=date(2026,1,2),
            dezenas=frozenset(range(11,26))
        )

    ])

    analyzer = HistoricoAnalyzer(historico)

    distribuicao = analyzer.distribuicao_colunas()

    assert distribuicao == {

        (3,3,3,3,3): 2

    }

