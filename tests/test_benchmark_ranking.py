import pytest
from benchmarks.benchmark_ranking import BenchmarkRanking
from benchmarks.benchmark_score import BenchmarkScore

from benchmarks.benchmark_table import BenchmarkTable
from benchmarks.benchmark_standing import BenchmarkStanding


def test_deve_atribuir_posicoes():

    ranking = BenchmarkRanking([

        BenchmarkScore(
            estrategia="Bayes",
            atributo="rmse",
            metrica="media",
            valor=0.10
        ),

        BenchmarkScore(
            estrategia="Markov",
            atributo="rmse",
            metrica="media",
            valor=0.20
        ),

        BenchmarkScore(
            estrategia="IA",
            atributo="rmse",
            metrica="media",
            valor=0.30
        ),

    ])

    assert ranking[0].posicao == 1

    assert ranking[1].posicao == 2

    assert ranking[2].posicao == 3

def test_deve_retornar_primeiro():

    ranking = BenchmarkRanking([

        BenchmarkScore("Bayes", "rmse", "media", 0.10),

        BenchmarkScore("Markov", "rmse", "media", 0.20),

    ])

    assert ranking.primeiro().estrategia == "Bayes"

def test_deve_retornar_ultimo():

    ranking = BenchmarkRanking([

        BenchmarkScore("Bayes", "rmse", "media", 0.10),

        BenchmarkScore("Markov", "rmse", "media", 0.20),

    ])

    assert ranking.ultimo().estrategia == "Markov"
    
def test_deve_retornar_top():

    ranking = BenchmarkRanking([

        BenchmarkScore("Bayes", "rmse", "media", 0.10),

        BenchmarkScore("Markov", "rmse", "media", 0.20),

        BenchmarkScore("IA", "rmse", "media", 0.30),

    ])

    top = ranking.top(2)

    assert len(top) == 2

    assert top.primeiro().estrategia == "Bayes"

    assert top.ultimo().estrategia == "Markov"
    
def test_deve_retornar_bottom():

    ranking = BenchmarkRanking([

        BenchmarkScore("Bayes", "rmse", "media", 0.10),

        BenchmarkScore("Markov", "rmse", "media", 0.20),

        BenchmarkScore("IA", "rmse", "media", 0.30),

    ])

    bottom = ranking.bottom(2)

    assert len(bottom) == 2

    assert bottom.primeiro().estrategia == "Markov"

    assert bottom.ultimo().estrategia == "IA"
    
def test_deve_obter_score_por_estrategia():

    ranking = BenchmarkRanking([

        BenchmarkScore(
            estrategia="Bayes",
            atributo="nota",
            metrica="rmse",
            valor=1
        ),

        BenchmarkScore(
            estrategia="Markov",
            atributo="nota",
            metrica="rmse",
            valor=2
        )

    ])

    score = ranking.obter("Bayes")

    assert score.estrategia == "Bayes"

    assert score.valor == 1
    
def test_deve_retornar_estrategias():

    ranking = BenchmarkRanking([

        BenchmarkScore("Bayes", "rmse", "media", 0.10),

        BenchmarkScore("Markov", "rmse", "media", 0.20),

    ])

    assert ranking.estrategias() == (

        "Bayes",

        "Markov"

    )
    
def test_deve_retornar_valores():

    ranking = BenchmarkRanking([

        BenchmarkScore(
            estrategia="Bayes",
            atributo="nota",
            metrica="rmse",
            valor=1
        ),

        BenchmarkScore(
            estrategia="Markov",
            atributo="nota",
            metrica="rmse",
            valor=2
        ),

        BenchmarkScore(
            estrategia="Interpolação",
            atributo="nota",
            metrica="rmse",
            valor=3
        )

    ])

    assert ranking.valores() == (

        1,

        2,

        3

    )
    
def test_deve_conter_estrategia():

    ranking = BenchmarkRanking([

        BenchmarkScore("Bayes", "rmse", "media", 0.10),

    ])

    assert "Bayes" in ranking

    assert "IA" not in ranking
    
def test_deve_lancar_erro_para_estrategia_inexistente():

    ranking = BenchmarkRanking([

        BenchmarkScore("Bayes", "rmse", "media", 0.10),

    ])

    with pytest.raises(KeyError):

        ranking.obter("IA")

def test_deve_ser_iteravel():

    ranking = BenchmarkRanking([

        BenchmarkScore("Bayes", "rmse", "media", 0.10),

        BenchmarkScore("Markov", "rmse", "media", 0.20),

    ])

    assert [

        score.estrategia

        for score in ranking

    ] == [

        "Bayes",

        "Markov"

    ]

def test_deve_retornar_quantidade():

    tabela = BenchmarkTable([

        BenchmarkStanding("Bayes", 5),

        BenchmarkStanding("Markov", 4)

    ])

    assert len(tabela) == 2
    
