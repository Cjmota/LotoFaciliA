from benchmarks.benchmark_league import BenchmarkLeague

from benchmarks.benchmark_leaderboard import BenchmarkLeaderboard

def test_deve_criar_campeonato():

    campeonato = BenchmarkLeague(

        BenchmarkLeaderboard({})

    )

    assert campeonato.leaderboard is not None