from analysis.statistics_result import StatisticsResult

def test_deve_criar_statistics_result():

    result = StatisticsResult()

    assert result.soma is None
    assert result.pares is None
    assert result.impares is None
    assert result.consecutivos is None