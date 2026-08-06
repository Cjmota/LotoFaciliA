from engine.history_repository import HistoryRepository
from engine.statistics_engine import StatisticsEngine

repo = HistoryRepository()

historico = repo.historico()

engine = StatisticsEngine(historico)

resultado = engine.calcular()

for nome, estatistica in resultado.items():

    print()

    print("=" * 40)

    print(nome)

    print("=" * 40)

    print(estatistica.distribuicao)