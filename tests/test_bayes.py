import pytest
from analysis.bayes import Bayes
from analysis.bayes import BayesEvidence

def test_deve_calcular_probabilidade_posterior():

    bayes = Bayes()

    posterior = bayes.posterior(

        priori=0.5,

        evidencias=[

            BayesEvidence(0.8),

            BayesEvidence(0.4)

        ]

    )

    assert posterior == pytest.approx(0.16)