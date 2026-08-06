from math import sqrt

from dataclasses import dataclass

from analysis.historico_analyzer import HistoricoAnalyzer


@dataclass(slots=True)
class HistoricoStatistics:

    analyzer: HistoricoAnalyzer

    def media(
        self,
        distribuicao: dict[int, int]
    ) -> float:

        total = sum(

            valor * quantidade

            for valor, quantidade in distribuicao.items()

        )

        elementos = sum(

            distribuicao.values()

        )
        
        if elementos == 0:

            return 0

        return total / elementos
    
    def mediana(
        self,
        distribuicao: dict[int, int]
    ) -> float:

        valores = []

        for valor, quantidade in distribuicao.items():

            valores.extend(

                [valor] * quantidade

            )

        valores.sort()

        meio = len(valores) // 2

        if len(valores) % 2 == 0:

            return (

                valores[meio - 1] +
                valores[meio]

            ) / 2

        return valores[meio]
    
    def variancia(
        self,
        distribuicao: dict[int, int]
    ) -> float:

        quantidade = sum(

            distribuicao.values()

        )

        if quantidade == 0:

            return 0

        media = self.media(distribuicao)

        soma = sum(

            ((valor - media) ** 2) * quantidade

            for valor, quantidade in distribuicao.items()

        )

        return soma / quantidade

    def desvio_padrao(
        self,
        distribuicao: dict[int, int]
    ) -> float:

        return sqrt(

            self.variancia(distribuicao)

        )
    
    def moda(
        self,
        distribuicao: dict[int, int]
    ) -> int:

        return max(

            distribuicao,

            key=distribuicao.get

        )
    
    def amplitude(
        self,
        distribuicao: dict[int, int]
    ) -> int:

        return max(distribuicao) - min(distribuicao)

    def probabilidades(
        self,
        distribuicao: dict[int, int]
    ) -> dict[int, float]:

        total = sum(distribuicao.values())

        return {

            valor: quantidade / total

            for valor, quantidade in distribuicao.items()

        }
    
    def probabilidade(
        self,
        valor: int,
        distribuicao: dict[int, int]
    ) -> float:

        return self.probabilidades(

            distribuicao

        ).get(valor, 0.0)
     
    def ranking(
        self,
        distribuicao: dict[int, int]
    ) -> list[tuple[int, int]]:

        return sorted(

            distribuicao.items(),

            key=lambda item: item[1],

            reverse=True

        )
    
    def mais_frequentes(
        self,
        distribuicao,
        quantidade
    ):

        return self.ranking(

            distribuicao

        )[:quantidade]
    
    def menos_frequentes(
        self,
        distribuicao,
        quantidade
    ):

        return self.ranking(

            distribuicao

        )[-quantidade:]
        
    def zscore(
        self,
        valor,
        distribuicao: dict[int, int]
    ) -> float:

        media = self.media(distribuicao)

        desvio = self.desvio_padrao(distribuicao)

        if desvio == 0:

            return 0

        return (

            valor - media

        ) / desvio
    
