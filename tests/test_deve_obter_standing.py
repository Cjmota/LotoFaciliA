from benchmarks.benchmark_table import BenchmarkTable
from benchmarks.benchmark_standing import BenchmarkStanding


def test_deve_obter_standing():

    tabela = BenchmarkTable([

        BenchmarkStanding(
            estrategia="Bayes",
            pontos=5
        ),

        BenchmarkStanding(
            estrategia="Markov",
            pontos=4
        )

    ])

    standing = tabela.obter("Bayes")

    assert standing.pontos == 5
