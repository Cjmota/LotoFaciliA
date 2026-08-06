from benchmarks.benchmark_result import BenchmarkResult
from benchmarks.benchmark_statistics import BenchmarkStatistics
from benchmarks.benchmark_metrics import BenchmarkMetrics
from benchmarks.benchmark_report import BenchmarkReport

from modelos.weight import Weight


def test_deve_calcular_mae_da_nota():

    resultados = [

        BenchmarkResult(

            categoria="Pares",

            valor=10,

            real=Weight(
                nota=80
            ),

            estimado=Weight(
                nota=90
            )

        ),

        BenchmarkResult(

            categoria="Pares",

            valor=20,

            real=Weight(
                nota=100
            ),

            estimado=Weight(
                nota=90
            )

        )

    ]

    stats = BenchmarkStatistics(
        resultados
    )

    assert stats.mae("nota") == 10
    
    
def test_deve_calcular_rmse_da_nota():

    resultados = [

        BenchmarkResult(

            categoria="Pares",

            valor=10,

            real=Weight(nota=80),

            estimado=Weight(nota=90)

        ),

        BenchmarkResult(

            categoria="Pares",

            valor=20,

            real=Weight(nota=100),

            estimado=Weight(nota=90)

        )

    ]

    stats = BenchmarkStatistics(resultados)

    assert stats.rmse("nota") == 10
    
def test_deve_gerar_resumo():

    resultados = [

        BenchmarkResult(

            categoria="Pares",

            valor=10,

            real=Weight(nota=80),

            estimado=Weight(nota=90)

        ),

        BenchmarkResult(

            categoria="Pares",

            valor=20,

            real=Weight(nota=100),

            estimado=Weight(nota=90)

        )

    ]

    stats = BenchmarkStatistics(resultados)

    resumo = stats.resumo("nota")

    assert resumo.atributo == "nota"

    assert resumo.quantidade == 2

    assert resumo.mae == 10

    assert resumo.rmse == 10

    assert resumo.erro_maximo == 10

    assert resumo.erro_minimo == 10

    assert resumo.mediana == 10

    assert resumo.desvio_padrao == 0
    

def test_deve_gerar_resumo_completo():

    resultados = [

        BenchmarkResult(

            categoria="Pares",

            valor=10,

            real=Weight(

                nota=80,

                probabilidade=0.70,

                peso_bayes=1.2,

                percentual=55

            ),

            estimado=Weight(

                nota=90,

                probabilidade=0.60,

                peso_bayes=1.1,

                percentual=50

            )

        ),

        BenchmarkResult(

            categoria="Pares",

            valor=20,

            real=Weight(

                nota=100,

                probabilidade=0.80,

                peso_bayes=1.5,

                percentual=60

            ),

            estimado=Weight(

                nota=90,

                probabilidade=0.75,

                peso_bayes=1.4,

                percentual=58

            )

        )

    ]

    stats = BenchmarkStatistics(resultados)

    resumo = stats.resumo_completo()

    assert isinstance(resumo, BenchmarkReport)

    assert "nota" in resumo.metricas
    assert "probabilidade" in resumo.metricas
    assert "peso_bayes" in resumo.metricas
    assert "percentual" in resumo.metricas

    assert resumo.metricas["nota"].mae == 10
    assert resumo.metricas["nota"].rmse == 10
    
    assert len(resumo.metricas) == len(Weight.atributos_benchmark())
    

def test_report_deve_retornar_atributos():

    metricas = BenchmarkMetrics(

        atributo="nota",

        quantidade=2,

        mae=1.5,

        rmse=2.0,

        erro_maximo=3.0,

        erro_minimo=1.0,

        mediana=1.5,

        desvio_padrao=0.7

    )

    report = BenchmarkReport({

        "nota": metricas

    })

    assert report.atributos == ("nota",)
    
