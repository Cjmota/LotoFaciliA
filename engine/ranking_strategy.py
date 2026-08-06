from abc import ABC, abstractmethod


class RankingStrategy(ABC):

    @abstractmethod
    def calcular(self, game):

        pass

class ScoreRanking(RankingStrategy):

    def calcular(self, game):

        return game.score_total

class ProbabilityRanking(RankingStrategy):

    def calcular(self, game):

        return game.probabilidade

class HybridRanking(RankingStrategy):

    def calcular(self, game):

        return (

            game.score_total * 0.70 +

            game.probabilidade * 0.30

        )

