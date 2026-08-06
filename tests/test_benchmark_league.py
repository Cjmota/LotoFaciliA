from benchmarks.benchmark_ranking import BenchmarkRanking

from benchmarks.benchmark_leaderboard import BenchmarkLeaderboard

from benchmarks.benchmark_score import BenchmarkScore

from benchmarks.benchmark_league import BenchmarkLeague

from benchmarks.linear_points_strategy import LinearPointsStrategy

from benchmarks.benchmark_table import BenchmarkTable

def criar_campeonato(
    ranking_rmse: BenchmarkRanking,
    ranking_mae: BenchmarkRanking
) -> BenchmarkLeague:

    leaderboard = BenchmarkLeaderboard({

        "rmse": ranking_rmse,

        "mae": ranking_mae

    })

    return BenchmarkLeague(

        leaderboard,

        LinearPointsStrategy()

    )

def ranking(
    atributo: str,
    estrategias: list[str]
) -> BenchmarkRanking:

    return BenchmarkRanking([

        BenchmarkScore(

            estrategia,

            atributo,

            "media",

            indice

        )

        for indice, estrategia in enumerate(

            estrategias,

            start=1

        )

    ])

def test_deve_contabilizar_vitorias():

    ranking_rmse = ranking("rmse", ["Bayes", "Markov", "IA"])

    ranking_mae = ranking("mae", ["Bayes", "IA", "Markov"])

    campeonato = criar_campeonato(

        ranking_rmse,

        ranking_mae

    )

    tabela = campeonato.calcular()

    assert tabela.obter("Bayes").vitorias == 2

def test_deve_somar_pontos():

    ranking_rmse = ranking("rmse", ["Bayes", "Markov", "IA"])

    ranking_mae = ranking("mae", ["IA", "Bayes", "Markov"])

    campeonato = criar_campeonato(

        ranking_rmse,

        ranking_mae

    )

    tabela = campeonato.calcular()

    assert tabela.obter("Bayes").pontos == 5
    assert tabela.obter("Markov").pontos == 3
    assert tabela.obter("IA").pontos == 4
    
def test_deve_retornar_benchmark_table():

    ranking_rmse = ranking("rmse", ["Bayes", "Markov", "IA"])

    ranking_mae = ranking("mae", ["IA", "Bayes", "Markov"])

    campeonato = criar_campeonato(

        ranking_rmse,

        ranking_mae

    )

    tabela = campeonato.calcular()

    assert isinstance(tabela, BenchmarkTable)
    
