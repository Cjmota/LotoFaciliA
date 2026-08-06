from benchmarks.benchmark_table import BenchmarkTable
from benchmarks.benchmark_standing import BenchmarkStanding


def test_deve_ordenar_por_segundos():

    tabela = BenchmarkTable([

        BenchmarkStanding(
            estrategia="Bayes",
            pontos=20,
            vitorias=1,
            segundos=2,
            terceiros=1
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
            segundos=0,
            terceiros=1
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
    
    