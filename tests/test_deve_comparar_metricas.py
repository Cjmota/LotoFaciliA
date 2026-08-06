from benchmarks.benchmark_report import BenchmarkReport

from benchmarks.benchmark_metrics import BenchmarkMetrics

from benchmarks.benchmark_comparison import BenchmarkComparison


def test_benchmark_comparison():  

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
    
    resultado = comparacao._comparar(

        "nota",

        "rmse"

    )
    
    assert resultado == [

        ("Bayes", 2),

        ("Interpolação", 1)

    ]