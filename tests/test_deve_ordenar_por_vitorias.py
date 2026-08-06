from benchmarks.benchmark_standing import BenchmarkStanding
from benchmarks.benchmark_table import BenchmarkTable


def test_ordenar_por_vitorias():
    tabela = BenchmarkTable([

        BenchmarkStanding(
            estrategia="Bayes",
            pontos=20,
            vitorias=2,
            segundos=1,
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
            vitorias=0,
            segundos=1,
            terceiros=1
        ),

    ])

    assert [
        standing.estrategia
        for standing in tabela
    ] == [
        "Bayes",
        "Markov",
        "IA"
    ]