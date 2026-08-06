from benchmarks.benchmark_standing import BenchmarkStanding
from benchmarks.benchmark_table import BenchmarkTable
from benchmarks.benchmark_table import BenchmarkTable



def test_deve_ordenar_por_pontos():

    tabela = BenchmarkTable([

        BenchmarkStanding(
            estrategia="Bayes",
            pontos=20,
            vitorias=1,
            segundos=1,
            terceiros=1
        ),

        BenchmarkStanding(
            estrategia="Markov",
            pontos=10,
            vitorias=1,
            segundos=1,
            terceiros=1
        ),

        BenchmarkStanding(
            estrategia="IA",
            pontos=30,
            vitorias=1,
            segundos=1,
            terceiros=1
        ),

    ])

    assert [
        standing.estrategia
        for standing in tabela
    ] == [
        "IA",
        "Bayes",
        "Markov"
    ]