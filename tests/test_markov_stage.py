from datetime import date
from analysis.feature_metadata import FeatureMetadata
from analysis.feature import Feature
from analysis.markov_builder import MarkovBuilder
from analysis.markov_stage import MarkovStage
from domain.concurso import Concurso
from domain.historico import Historico


def test_deve_adicionar_probabilidade_markov():

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
        )

    ])

    cadeia = MarkovBuilder().construir_somas(

        historico

    )

    stage = MarkovStage(

        cadeia,

        lambda feature: feature.soma,

        FeatureMetadata.MARKOV_SOMA

    )

    feature = Feature(

        soma=120,

        pares=7,

        impares=8,

        consecutivos=14,

        linhas=(5,5,5,0,0),

        colunas=(3,3,3,3,3)

    )

    resultado = stage.processar(

        feature

    )

    assert resultado.metadata[
        FeatureMetadata.MARKOV_SOMA
    ] == 1.0
