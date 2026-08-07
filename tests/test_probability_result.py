from analysis.probability_result import ProbabilityResult


def test_deve_criar_probability_result():

    result = ProbabilityResult()

    assert result.soma is None

    assert result.pares is None

    assert result.impares is None

    assert result.consecutivos is None

    assert result.linhas is None

    assert result.colunas is None