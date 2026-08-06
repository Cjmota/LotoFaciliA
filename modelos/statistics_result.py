from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class StatisticsResult:

    nome: str

    distribuicao: dict[Any, int]

    @property
    def total(self):

        return sum(

            self.distribuicao.values()

        )

    @property
    def quantidade_valores(self):

        return len(

            self.distribuicao

        )

    @property
    def moda(self):

        return max(

            self.distribuicao,

            key=self.distribuicao.get

        )

    @property
    def minimo(self):

        return min(

            self.distribuicao

        )

    @property
    def maximo(self):

        return max(

            self.distribuicao

        )

    @property
    def frequencia_maxima(self):

        return max(

            self.distribuicao.values()

        )

    @property
    def valores(self):

        return tuple(

            self.distribuicao.keys()

        )

    @property
    def frequencias(self):

        return tuple(

            self.distribuicao.values()

        )

    def __repr__(self):

        return (

            f"{self.nome}"

            f" ({len(self.distribuicao)} valores)"

        )
        
