from benchmarks.benchmark_table import BenchmarkTable

from benchmarks.benchmark_standing import BenchmarkStanding

def test_primeiro_deve_retornar_o_primeiro_standing():

    tabela = BenchmarkTable([

        BenchmarkStanding("Bayes", 10),

        BenchmarkStanding("Markov", 8),

        BenchmarkStanding("IA", 6),

    ])

    assert tabela.primeiro().estrategia == "Bayes"