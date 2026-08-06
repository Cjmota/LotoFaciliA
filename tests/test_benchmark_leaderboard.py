from benchmarks.benchmark_leaderboard import BenchmarkLeaderboard
from benchmarks.benchmark_ranking import BenchmarkRanking
from benchmarks.benchmark_table import BenchmarkTable
from benchmarks.benchmark_standing import BenchmarkStanding

def test_deve_retornar_metricas():

    leaderboard = BenchmarkLeaderboard({

        "rmse": BenchmarkRanking([]),

        "mae": BenchmarkRanking([]),

        "desvio_padrao": BenchmarkRanking([])

    })

    assert leaderboard.metricas == (

        "rmse",

        "mae",

        "desvio_padrao"

    )

def test_deve_obter_ranking():

    leaderboard = BenchmarkLeaderboard({

        "rmse": BenchmarkRanking([])

    })

    ranking = BenchmarkRanking([])

    leaderboard = BenchmarkLeaderboard({

        "rmse": ranking

    })

    assert leaderboard.obter("rmse") is ranking
    
def test_deve_suportar_indice():

    leaderboard = BenchmarkLeaderboard({

        "rmse": BenchmarkRanking([])

    })

    ranking = leaderboard["rmse"]

    assert leaderboard.obter("rmse") is ranking
    
def test_deve_conter_metrica():

    leaderboard = BenchmarkLeaderboard({

        "rmse": BenchmarkRanking([])

    })

    assert "rmse" in leaderboard

    assert "mae" not in leaderboard

def test_deve_retornar_quantidade():

    leaderboard = BenchmarkLeaderboard({

        "rmse": BenchmarkRanking([]),

        "mae": BenchmarkRanking([])

    })

    assert len(leaderboard) == 2

def test_deve_ser_iteravel():

    leaderboard = BenchmarkLeaderboard({

        "rmse": BenchmarkRanking([]),

        "mae": BenchmarkRanking([])

    })

    assert [

        metrica

        for metrica, _ in leaderboard

    ] == [

        "rmse",

        "mae"

    ]

