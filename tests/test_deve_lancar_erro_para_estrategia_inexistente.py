import pytest

from benchmarks.benchmark_ranking import BenchmarkRanking
from benchmarks.benchmark_score import BenchmarkScore


def test_deve_lancar_erro_para_estrategia_inexistente():

    ranking = BenchmarkRanking([

        BenchmarkScore("Bayes", "rmse", "media", 0.10),

    ])

    with pytest.raises(KeyError):

        ranking.obter("IA")