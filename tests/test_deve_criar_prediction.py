from analysis import prediction
from analysis import feature
from analysis.feature import Feature
from analysis.prediction import Prediction
from analysis.probability_result import ProbabilityResult
from analysis.statistics_result import StatisticsResult
from analysis.markov_result import MarkovResult


def test_deve_criar_prediction():

    feature = Feature(

        soma=120,

        pares=7,

        impares=8,

        consecutivos=14,

        linhas=(5,5,5,0,0),

        colunas=(3,3,3,3,3)

    )

    prediction = Prediction(

        feature

    )

    assert prediction.feature == feature

    assert isinstance(

        prediction.analysis.probability,

        ProbabilityResult

    )
    
    assert isinstance(
        prediction.analysis.statistics,
        StatisticsResult
    )
    assert prediction.analysis.bayes == {}
    assert prediction.analysis.markov.soma is None
    assert prediction.analysis.score == {}