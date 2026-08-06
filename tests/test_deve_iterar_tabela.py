from benchmarks.benchmark_table import BenchmarkTable
from benchmarks.benchmark_standing import BenchmarkStanding

def test_deve_iterar_tabela():

    tabela = BenchmarkTable([

        BenchmarkStanding("Bayes", 5),

        BenchmarkStanding("Markov", 4)

    ])

    assert len(list(tabela)) == 2