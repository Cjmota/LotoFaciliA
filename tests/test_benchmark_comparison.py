from benchmarks.benchmark_comparison import BenchmarkComparison

from benchmarks.benchmark_report import BenchmarkReport



def test_deve_retornar_nomes_das_estrategias():

    comparacao = BenchmarkComparison({

        "Bayes": BenchmarkReport({}),

        "Interpolacao": BenchmarkReport({})

    })

    assert comparacao.nomes == (
        "Bayes",
        "Interpolacao"
    )

def test_deve_obter_relatorio():

    report = BenchmarkReport({})

    comparacao = BenchmarkComparison({

        "Bayes": report

    })

    assert comparacao.obter("Bayes") is report

def test_deve_suportar_indexacao():

    report = BenchmarkReport({})

    comparacao = BenchmarkComparison({

        "Bayes": report

    })

    assert comparacao["Bayes"] is report


def test_deve_conter_estrategia():

    comparacao = BenchmarkComparison({

        "Bayes": BenchmarkReport({})

    })

    assert "Bayes" in comparacao


def test_deve_retornar_quantidade_de_estrategias():

    comparacao = BenchmarkComparison({

        "Bayes": BenchmarkReport({}),

        "Interpolacao": BenchmarkReport({})

    })

    assert len(comparacao) == 2

def test_deve_iterar_estrategias():

    comparacao = BenchmarkComparison({

        "Bayes": BenchmarkReport({})

    })

    itens = list(comparacao)

    assert itens[0][0] == "Bayes"