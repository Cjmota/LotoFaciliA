import pytest
from analysis.bayes import Bayes
from analysis.bayes_stage import BayesStage
from analysis.feature import Feature


def test_deve_adicionar_probabilidade_bayes():

    stage = BayesStage(

        Bayes()

    )

    feature = Feature(

        soma=120,

        pares=7,

        impares=8,

        consecutivos=14,

        linhas=(5,5,5,0,0),

        colunas=(3,3,3,3,3),

        metadata={

            "score": 0.50,

            "prob_soma": 0.80,

            "prob_pares": 0.40

        }

    )

    resultado = stage.processar(feature)

    assert resultado.metadata["bayes"] == pytest.approx(0.16)