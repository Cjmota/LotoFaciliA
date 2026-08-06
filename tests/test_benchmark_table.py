import pytest
from benchmarks.benchmark_standing import BenchmarkStanding
from benchmarks.benchmark_table import BenchmarkTable


def test_deve_ordenar_por_pontos():

    tabela = BenchmarkTable([

        BenchmarkStanding(
            estrategia="Bayes",
            pontos=20,
            vitorias=1,
            segundos=1,
            terceiros=1
        ),

        BenchmarkStanding(
            estrategia="Markov",
            pontos=10,
            vitorias=1,
            segundos=1,
            terceiros=1
        ),

        BenchmarkStanding(
            estrategia="IA",
            pontos=30,
            vitorias=1,
            segundos=1,
            terceiros=1
        ),

    ])

    assert [
        standing.estrategia
        for standing in tabela
    ] == [
        "IA",
        "Bayes",
        "Markov"
    ]

def test_deve_ordenar_por_vitorias():
    tabela = BenchmarkTable([

        BenchmarkStanding(
            estrategia="Bayes",
            pontos=20,
            vitorias=2,
            segundos=1,
            terceiros=1
        ),

        BenchmarkStanding(
            estrategia="Markov",
            pontos=20,
            vitorias=1,
            segundos=1,
            terceiros=1
        ),

        BenchmarkStanding(
            estrategia="IA",
            pontos=20,
            vitorias=0,
            segundos=1,
            terceiros=1
        ),

    ])

    assert [
        standing.estrategia
        for standing in tabela
    ] == [
        "Bayes",
        "Markov",
        "IA"
    ]

def test_deve_ordenar_por_segundos():

    tabela = BenchmarkTable([

        BenchmarkStanding(
            estrategia="Bayes",
            pontos=20,
            vitorias=1,
            segundos=2,
            terceiros=1
        ),

        BenchmarkStanding(
            estrategia="Markov",
            pontos=20,
            vitorias=1,
            segundos=1,
            terceiros=1
        ),

        BenchmarkStanding(
            estrategia="IA",
            pontos=20,
            vitorias=1,
            segundos=0,
            terceiros=1
        ),

    ])

    assert [
        standing.estrategia
        for standing in tabela
    ] == [
        "IA",
        "Markov",
        "Bayes"
    ]
    
def test_deve_ordenar_por_terceiros():

    tabela = BenchmarkTable([

        BenchmarkStanding(
            estrategia="Bayes",
            pontos=20,
            vitorias=1,
            segundos=1,
            terceiros=2
        ),

        BenchmarkStanding(
            estrategia="Markov",
            pontos=20,
            vitorias=1,
            segundos=1,
            terceiros=1
        ),

        BenchmarkStanding(
            estrategia="IA",
            pontos=20,
            vitorias=1,
            segundos=1,
            terceiros=0
        ),

    ])

    assert [
        standing.estrategia
        for standing in tabela
    ] == [
        "IA",
        "Markov",
        "Bayes"
    ]

def test_deve_retornar_primeiro():

    tabela = BenchmarkTable([

        BenchmarkStanding("Bayes", 5),
        BenchmarkStanding("Markov", 4),

    ])

    assert tabela.primeiro().estrategia == "Bayes"

def test_deve_retornar_ultimo():

    tabela = BenchmarkTable([

        BenchmarkStanding("Bayes", 5),
        BenchmarkStanding("Markov", 4),

    ])

    assert tabela.ultimo().estrategia == "Markov"

def test_deve_retornar_top():

    tabela = BenchmarkTable([

        BenchmarkStanding("Bayes", 0.10),
        BenchmarkStanding("Markov", 0.20),
        BenchmarkStanding("IA", 0.30),

    ])

    top = tabela.top(2)

    assert len(top) == 2

    assert top[0].estrategia == "IA"

    assert top[1].estrategia == "Markov"

def test_deve_retornar_bottom():

    tabela = BenchmarkTable([

        BenchmarkStanding("Bayes", 0.10),
        BenchmarkStanding("Markov", 0.20),
        BenchmarkStanding("IA", 0.30),

    ])

    bottom = tabela.bottom(2)

    assert len(bottom) == 2

    assert bottom[0].estrategia == "Markov"

    assert bottom[1].estrategia == "Bayes"

def test_deve_obter_standing():

    tabela = BenchmarkTable([

        BenchmarkStanding(
            estrategia="Bayes",
            pontos=5
        ),

        BenchmarkStanding(
            estrategia="Markov",
            pontos=4
        )

    ])

    standing = tabela.obter("Bayes")

    assert standing.pontos == 5

def test_deve_lancar_erro_para_estrategia_inexistente():

    tabela = BenchmarkTable([

        BenchmarkStanding("Bayes", 5),

    ])

    with pytest.raises(KeyError):

        tabela.obter("IA")
        
def test_deve_conter_estrategia():

    tabela = BenchmarkTable([

        BenchmarkStanding(
            estrategia="Bayes",
            pontos=5
        ),

        BenchmarkStanding(
            estrategia="Markov",
            pontos=4
        )

    ])

    assert "Bayes" in tabela

    assert "IA" not in tabela

def test_deve_ser_iteravel():

    tabela = BenchmarkTable([

        BenchmarkStanding("Bayes", 5),
        BenchmarkStanding("Markov", 4),
        BenchmarkStanding("IA", 3)

    ])

    assert [

        standing.estrategia

        for standing in tabela

    ] == [

        "Bayes",

        "Markov",

        "IA"

    ]

def test_deve_retornar_quantidade():

    tabela = BenchmarkTable([

        BenchmarkStanding("Bayes", 5),

        BenchmarkStanding("Markov", 4),

        BenchmarkStanding("IA", 3),

    ])

    assert len(tabela) == 3
    
