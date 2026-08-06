from benchmarks.benchmark_metrics import BenchmarkMetrics
from benchmarks.benchmark_report import BenchmarkReport
from benchmarks.benchmark_comparison import BenchmarkComparison


def test_deve_ordenar_metricas():

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

    report3 = BenchmarkReport({
        "nota": BenchmarkMetrics(
            atributo="nota",
            quantidade=2,
            mae=3,
            rmse=3,
            erro_maximo=4,
            erro_minimo=2,
            mediana=3,
            desvio_padrao=0.8
        )
    })

    comparacao = BenchmarkComparison({

        "Bayes": report1,

        "Interpolação": report2,

        "Markov": report3

    })

    resultado = comparacao._ordenar(

        "nota",

        "rmse"

    )

    assert [s.estrategia for s in resultado] == [
        "Interpolação",
        "Bayes",
        "Markov"
    ]

    assert [s.valor for s in resultado] == [
        1,
        2,
        3
    ]