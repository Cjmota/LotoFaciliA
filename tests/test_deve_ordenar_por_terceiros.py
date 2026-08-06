from benchmarks.benchmark_standing import BenchmarkStanding
from benchmarks.benchmark_table import BenchmarkTable


def test_deve_ordenar_por_terceiros():

    tabela = BenchmarkTable([

        BenchmarkStanding(
            estrategia="Bayes",
            pontos=20,
            vitorias=1,
            segundos=1,
            terceiros=2
        ),

        BenchmarkStanding(
            estrategia="Markov",
            pontos=20,
            vitorias=1,
            segundos=1,
            terceiros=1
        ),

        BenchmarkStanding(
            estrategia="IA",
            pontos=20,
            vitorias=1,
            segundos=1,
            terceiros=0
        ),

    ])

    assert [
        standing.estrategia
        for standing in tabela
    ] == [
        "IA",
        "Markov",
        "Bayes"
    ]