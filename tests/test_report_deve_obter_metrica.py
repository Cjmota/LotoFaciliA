from benchmarks.benchmark_report import BenchmarkReport

from benchmarks.benchmark_metrics import BenchmarkMetrics

from benchmarks.benchmark_comparison import BenchmarkComparison


def test_report_deve_obter_metrica():

    metricas = BenchmarkMetrics(

        atributo="nota",

        quantidade=2,

        mae=1,

        rmse=1,

        erro_maximo=1,

        erro_minimo=1,

        mediana=1,

        desvio_padrao=0

    )

    report = BenchmarkReport({

        "nota": metricas

    })

    assert report.metrica("nota") is metricas
    
