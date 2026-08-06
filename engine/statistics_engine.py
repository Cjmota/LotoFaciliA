
from engine.statistics.registry import STATISTICS


class StatisticsEngine:

    def __init__(self, historico):
        self.statistics = [cls(historico) for cls in STATISTICS]

    def calcular(self):
        return {
            statistic.nome: statistic.calcular()
            for statistic in self.statistics
        }
    
    
        
    