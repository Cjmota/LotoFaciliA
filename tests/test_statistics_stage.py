from analysis.feature import Feature
from analysis.feature_metadata import FeatureMetadata
from analysis.statistics_stage import StatisticsStage
from analysis.historico_analyzer import HistoricoAnalyzer
from analysis.historico_statistics import HistoricoStatistics
from domain.historico import Historico
from operator import attrgetter


def test_deve_adicionar_zscore_da_soma():

    analyzer = HistoricoAnalyzer(

        Historico([])

    )

    statistics = HistoricoStatistics(

        analyzer

    )

    stage = StatisticsStage(

        analyzer.distribuicao_somas,

        attrgetter("soma"),

        FeatureMetadata.ZSCORE_SOMA,

        statistics

        )

    feature = Feature(

        soma=120,

        pares=7,

        impares=8,

        consecutivos=14,

        linhas=(5,5,5,0,0),

        colunas=(3,3,3,3,3)

    )

    resultado = stage.processar(feature)

    assert FeatureMetadata.ZSCORE_SOMA in resultado.metadata

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