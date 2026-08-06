from engine.ranking_strategy import ScoreRanking

from collections.abc import Iterable

from engine.game import Game

class RankingEngine:

    def __init__(

        self,

        strategy=None

    ):

        self.strategy = strategy or ScoreRanking()
    
    
    def ordenar(
        self,
        jogos: Iterable[Game],
        reverse=True
    ) -> list[Game]:

        return sorted(
            jogos,
            key=self._key,
            reverse=reverse
        )

    
    def usar(self, strategy):

        self.strategy = strategy
        
        return self
    
    def melhores(

        self,

        jogos: Iterable[Game],

        quantidade: int = 100

    ) -> Iterable[Game]:

        return self.ordenar(jogos)[:quantidade]
    
    def piores(

        self,

        jogos: Iterable[Game],
        
        quantidade: int = 100

    ) -> Iterable[Game]:

        return self.ordenar(

            jogos,

            reverse=False

        )[:quantidade]
    
    def validos(

        self,

        jogos: Iterable[Game],

    ) -> Iterable[Game]:

        return [

            j

            for j in jogos

            if j.valido

        ]
    
    def invalidos(

        self,

        jogos: Iterable[Game],

    ) -> Iterable[Game]:

        return [

            j

            for j in jogos

            if not j.valido

        ]
    
    def resumo(
        self,
        jogos: Iterable[Game]
    ) -> dict:

        jogos = list(jogos)

        if not jogos:
            return {}

        return {

            "total": len(jogos),

            "melhor": max(
                j.score_total
                for j in jogos
            ),

            "pior": min(
                j.score_total
                for j in jogos
            ),

            "media": (
                sum(
                    j.score_total
                    for j in jogos
                )
                / len(jogos)
            )

        }
    
    def top(
        self,
        jogos: Iterable[Game],
        quantidade: int = 100
    ) -> Iterable[Game]:

        return self.melhores(

            jogos,

            quantidade

        )
    
    def bottom(
        self,
        jogos: Iterable[Game],
        quantidade: int = 100
    ) -> Iterable[Game]:

        return self.piores(
            jogos,
            quantidade
        )
    
    def filtrar(
        self,
        jogos: Iterable[Game],
        minimo: float
    ) -> Iterable[Game]:

        return [

            jogo

            for jogo in jogos

            if jogo.score_normalizado >= minimo

        ]
    
    def melhor(
        self,
        jogos: Iterable[Game]
    ) -> Game | None:
        
        return max(
            jogos,
            key=self._key,
            default=None
        )
    
    def pior(
        self,
        jogos: Iterable[Game]
    ) -> Game | None:

        return min(
            jogos,
            key=self._key,
            default=None
        )
    
    def top_percentual(
        self,
        jogos: Iterable[Game],
        percentual: float
    ) -> list[Game]:

        from math import ceil

        ranking = self.ordenar(jogos)

        quantidade = max(
            1,
            ceil(len(ranking) * percentual / 100)
        )

        return ranking[:quantidade]
    
    def limitar(

        self,

        jogos: Iterable[Game],

        quantidade: int

    ) -> list[Game]:

        jogos = list(jogos)

        return jogos[:quantidade]
    
    @property
    def _key(self):
        return self.strategy.calcular