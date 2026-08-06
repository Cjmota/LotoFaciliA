from engine.history_repository import HistoryRepository
from engine.statistics_engine import StatisticsEngine
from weight.weight_generator import WeightGenerator
from weight.weight_writer import WeightWriter

repo = HistoryRepository()
historico = repo.historico()

stats = StatisticsEngine(historico)

generator = WeightGenerator(stats)

pesos = generator.gerar()

# Apenas para conferirmos
print(pesos.keys())

writer = WeightWriter()
writer.salvar(pesos)

print("Arquivo pesos_estatisticos.json gerado com sucesso!")