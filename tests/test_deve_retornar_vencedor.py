from benchmarks.benchmark_metrics import BenchmarkMetrics
from benchmarks.benchmark_report import BenchmarkReport
from benchmarks.benchmark_comparison import BenchmarkComparison
from benchmarks.benchmark_score import BenchmarkScore


def test_deve_retornar_vencedor():

    report1 = BenchmarkReport({
        "nota": BenchmarkMetrics(
            atributo="nota",
            quantidade=2,
            mae=2,
            rmse=2,
            erro_maximo=3,
            erro_minimo=1,
            mediana=2,
            desvio_padrao=0.5
        )
    })

    report2 = BenchmarkReport({
        "nota": BenchmarkMetrics(
            atributo="nota",
            quantidade=2,
            mae=1,
            rmse=1,
            erro_maximo=2,
            erro_minimo=1,
            mediana=1,
            desvio_padrao=0.2
        )
    })

    comparacao = BenchmarkComparison({
        "Bayes": report1,
        "Interpolação": report2
    })

    vencedor = comparacao.vencedor(
        "nota",
        "rmse"
    )

    assert isinstance(vencedor, BenchmarkScore)
    assert vencedor.estrategia == "Interpolação"
    assert vencedor.valor == 1