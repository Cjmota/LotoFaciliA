from engine.history_repository import HistoryRepository

repo = HistoryRepository()

historico = repo.historico()

print(max(c.baixas for c in historico))
print(min(c.baixas for c in historico))

print(max(c.altas for c in historico))
print(min(c.altas for c in historico))