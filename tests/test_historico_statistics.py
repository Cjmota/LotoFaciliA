from analysis.historico_analyzer import HistoricoAnalyzer
from analysis.historico_statistics import HistoricoStatistics
from domain.historico import Historico


def test_deve_criar_statistics():

    historico = Historico([])
    analyzer = HistoricoAnalyzer(historico)
    statistics = HistoricoStatistics(analyzer)
    assert statistics.analyzer is analyzer

def test_deve_calcular_media():

    analyzer = HistoricoAnalyzer(Historico([]))

    statistics = HistoricoStatistics(analyzer)

    distribuicao = {

        10: 2,

        20: 2

    }

    assert statistics.media(distribuicao) == 15
    
def test_deve_calcular_variancia():

    analyzer = HistoricoAnalyzer(Historico([]))

    statistics = HistoricoStatistics(analyzer)

    distribuicao = {

        10: 2,

        20: 2

    }

    assert statistics.variancia(distribuicao) == 25

def test_deve_calcular_desvio_padrao():

    analyzer = HistoricoAnalyzer(Historico([]))

    statistics = HistoricoStatistics(analyzer)

    distribuicao = {

        10: 2,

        20: 2

    }

    assert statistics.desvio_padrao(distribuicao) == 5

def test_deve_calcular_mediana():

    analyzer = HistoricoAnalyzer(Historico([]))

    statistics = HistoricoStatistics(analyzer)

    distribuicao = {

        10: 2,

        20: 2

    }

    assert statistics.mediana(distribuicao) == 15

def test_deve_calcular_mediana_impar():

    analyzer = HistoricoAnalyzer(Historico([]))

    statistics = HistoricoStatistics(analyzer)

    distribuicao = {

        10: 1,
        20: 1,
        30: 1

    }

    assert statistics.mediana(distribuicao) == 20

def test_deve_calcular_moda():

    analyzer = HistoricoAnalyzer(Historico([]))

    statistics = HistoricoStatistics(analyzer)

    distribuicao = {

        10: 5,

        20: 2,

        30: 1

    }

    assert statistics.moda(distribuicao) == 10

def test_deve_calcular_amplitude():

    analyzer = HistoricoAnalyzer(Historico([]))

    statistics = HistoricoStatistics(analyzer)

    distribuicao = {

        10: 2,
        20: 2,
        30: 1

    }

    assert statistics.amplitude(distribuicao) == 20

def test_deve_calcular_probabilidades():

    analyzer = HistoricoAnalyzer(Historico([]))

    statistics = HistoricoStatistics(analyzer)

    distribuicao = {

        7: 2,

        8: 3

    }

    probabilidades = statistics.probabilidades(distribuicao)

    assert probabilidades == {

        7: 0.4,

        8: 0.6

    }

def test_deve_obter_probabilidade():

    analyzer = HistoricoAnalyzer(Historico([]))

    statistics = HistoricoStatistics(analyzer)

    distribuicao = {

        7: 2,
        8: 3

    }

    assert statistics.probabilidade(

        8,

        distribuicao

    ) == 0.6

def test_deve_retornar_ranking():

    analyzer = HistoricoAnalyzer(Historico([]))

    statistics = HistoricoStatistics(analyzer)

    distribuicao = {

        7: 2,
        8: 5,
        9: 1

    }

    ranking = statistics.ranking(distribuicao)

    assert ranking == [

        (8, 5),

        (7, 2),

        (9, 1)

    ]
    
def test_deve_retornar_mais_frequentes():

    analyzer = HistoricoAnalyzer(Historico([]))

    statistics = HistoricoStatistics(analyzer)

    distribuicao = {

        7: 2,
        8: 5,
        9: 1

    }

    assert statistics.mais_frequentes(

        distribuicao,
        2

    ) == [

        (8, 5),

        (7, 2)

    ]

def test_deve_retornar_menos_frequentes():

    analyzer = HistoricoAnalyzer(Historico([]))

    statistics = HistoricoStatistics(analyzer)

    distribuicao = {

        7: 2,
        8: 5,
        9: 1

    }

    assert statistics.menos_frequentes(

        distribuicao,
        2

    ) == [

        (7, 2),

        (9, 1)

    ]

def test_deve_calcular_zscore():

    analyzer = HistoricoAnalyzer(Historico([]))

    statistics = HistoricoStatistics(analyzer)

    distribuicao = {

        10: 2,

        20: 2

    }

    assert statistics.zscore(

        15,

        distribuicao

    ) == 0
    
def test_media_de_distribuicao_vazia():

    analyzer = HistoricoAnalyzer(Historico([]))

    statistics = HistoricoStatistics(analyzer)

    assert statistics.media({}) == 0

def test_variancia_de_distribuicao_vazia():

    analyzer = HistoricoAnalyzer(Historico([]))

    statistics = HistoricoStatistics(analyzer)

    assert statistics.variancia({}) == 0

def test_desvio_padrao_de_distribuicao_vazia():

    analyzer = HistoricoAnalyzer(Historico([]))

    statistics = HistoricoStatistics(analyzer)

    assert statistics.desvio_padrao({}) == 0

def test_zscore_de_distribuicao_vazia():

    analyzer = HistoricoAnalyzer(Historico([]))

    statistics = HistoricoStatistics(analyzer)

    assert statistics.zscore(120, {}) == 0
