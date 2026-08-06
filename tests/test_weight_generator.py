from engine.history_repository import HistoryRepository
from engine.statistics_engine import StatisticsEngine
from weight.weight_generator import WeightGenerator
from weight.weight_writer import WeightWriter

repo = HistoryRepository()

historico = repo.historico()

stats = StatisticsEngine(historico)

generator = WeightGenerator(stats)

pesos = generator.gerar()

writer = WeightWriter()

writer.salvar(pesos)

print()
print("Arquivo gerado com sucesso!")
print()

print(pesos.keys())

print("=" * 40)
print("PARES")
print("=" * 40)

print(pesos["Pares"][7])