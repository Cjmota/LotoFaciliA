from analysis.analysis_builder import AnalysisBuilder
from analysis.feature import Feature
from analysis.markov_result import MarkovResult
from analysis.probability_result import ProbabilityResult
from analysis.statistics_result import StatisticsResult


def test_deve_construir_probability_result():

    feature = Feature(

        soma=120,

        pares=7,

        impares=8,

        consecutivos=14,

        linhas=(5, 5, 5, 0, 0),

        colunas=(3, 3, 3, 3, 3)

    )

    result = AnalysisBuilder().build(feature)

    assert isinstance(
        result.probability,
        ProbabilityResult
    )

def test_deve_construir_statistics_result():

    feature = Feature(

        soma=120,

        pares=7,

        impares=8,

        consecutivos=14,

        linhas=(5, 5, 5, 0, 0),

        colunas=(3, 3, 3, 3, 3)

    )

    result = AnalysisBuilder().build(feature)

    assert isinstance(
        result.statistics,
        StatisticsResult
    )

def test_deve_construir_markov_result():

    feature = Feature(

        soma=120,

        pares=7,

        impares=8,

        consecutivos=14,

        linhas=(5, 5, 5, 0, 0),

        colunas=(3, 3, 3, 3, 3)

    )

    result = AnalysisBuilder().build(feature)

    assert isinstance(
        result.markov,
        MarkovResult
    )
    
