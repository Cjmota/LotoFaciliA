from benchmarks.benchmark_table import BenchmarkTable
from benchmarks.benchmark_standing import BenchmarkStanding

def test_deve_retornar_quantidade():

    tabela = BenchmarkTable([

        BenchmarkStanding("Bayes", 5),

        BenchmarkStanding("Markov", 4)

    ])

    assert len(tabela) == 2

