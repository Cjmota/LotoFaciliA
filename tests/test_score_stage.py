from analysis.feature import Feature
from analysis.score_stage import ScoreStage


def test_deve_calcular_score():

    feature = Feature(

        soma=120,

        pares=7,

        impares=8,

        consecutivos=14,

        linhas=(5,5,5,0,0),

        colunas=(3,3,3,3,3),

        metadata={

            "prob_soma": 0.80,

            "prob_pares": 0.60

        }

    )

    stage = ScoreStage()

    resultado = stage.processar(feature)

    assert resultado.metadata["score"] == 0.70

def test_deve_retornar_score_zero():

    feature = Feature(

        soma=0,
        pares=0,
        impares=0,
        consecutivos=0,
        linhas=(0,0,0,0,0),
        colunas=(0,0,0,0,0)

    )

    resultado = ScoreStage().processar(feature)

    assert resultado.metadata["score"] == 0

