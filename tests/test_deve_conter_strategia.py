from benchmarks.benchmark_table import BenchmarkTable
from benchmarks.benchmark_standing import BenchmarkStanding


def test_deve_conter_estrategia():

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

    assert "Bayes" in tabela

    assert "IA" not in tabela