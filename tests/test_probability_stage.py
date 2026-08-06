from datetime import date

from analysis.feature import Feature
from analysis.feature_pipeline import FeaturePipeline
from analysis.probability_stage import ProbabilityStage
from analysis.historico_analyzer import HistoricoAnalyzer
from analysis.historico_statistics import HistoricoStatistics
from domain.concurso import Concurso
from domain.historico import Historico


def test_deve_adicionar_probabilidade_da_soma():

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

    statistics = HistoricoStatistics(analyzer)

    stage = ProbabilityStage(

        analyzer.distribuicao_somas,

        lambda feature: feature.soma,

        "prob_soma",

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

    assert resultado.metadata["prob_soma"] == 1.0
    