from abc import ABC
from typing import ClassVar
from collections import Counter
from modelos.statistics_result import StatisticsResult


class BaseStatistics(ABC):

    
    
    atributo: ClassVar[str | None] = None
    nome: ClassVar[str | None] = None

    def __init__(self, historico):

        self.historico = historico

    def calcular(self):
        
        if self.atributo is None:
            raise NotImplementedError(
                "atributo não definido."
            )

        if self.nome is None:
            raise NotImplementedError(
                "nome não definido."
            )

        distribuicao = Counter()

        for concurso in self.historico:

            valor = getattr(

                concurso,

                self.atributo

            )

            distribuicao[valor] += 1

        distribuicao = dict(

            sorted(

                distribuicao.items()

            )

        )

        return StatisticsResult(

            nome=self.nome,

            distribuicao=distribuicao

        )