from dataclasses import dataclass

from benchmarks.benchmark_report import BenchmarkReport

from benchmarks.benchmark_score import BenchmarkScore

from benchmarks.benchmark_ranking import BenchmarkRanking


@dataclass(slots=True)
class BenchmarkComparison:

    estrategias: dict[str, BenchmarkReport]

    @property
    def nomes(self) -> tuple[str, ...]:
        return tuple(self.estrategias.keys())
    
    def obter(self, estrategia: str) -> BenchmarkReport:
        return self.estrategias[estrategia]

    def __getitem__(self, estrategia: str) -> BenchmarkReport:
        return self.estrategias[estrategia]

    def __contains__(self, estrategia: str) -> bool:
        return estrategia in self.estrategias

    def __len__(self) -> int:
        return len(self.estrategias)

    def __iter__(self):
        return iter(self.estrategias.items())
    
    
    
    def _comparar(
        self,
        atributo: str,
        metrica: str
    ) -> list[tuple[str, float]]:

        comparacao = []

        for nome, report in self:

            metricas = report.metrica(atributo)

            valor = getattr(metricas, metrica)

            comparacao.append(

                (nome, valor)

            )

        return comparacao
    
    def _ordenar(
        self,
        atributo: str,
        metrica: str
    ) -> list[BenchmarkScore]:

        dados = self._comparar(

            atributo,

            metrica

        )

        dados = sorted(

            dados,

            key=lambda item: item[1]

        )

        scores = []

        for estrategia, valor in dados:

            scores.append(

                BenchmarkScore(

                    estrategia=estrategia,

                    atributo=atributo,

                    metrica=metrica,

                    valor=valor

                )

            )

        return scores
    
    
    def vencedor(
        self,
        atributo: str,
        metrica: str
    ) -> BenchmarkScore:

        return self.ranking(
            atributo,
            metrica
        ).primeiro()
    

    def ranking(
        self,
        atributo: str,
        metrica: str
    ) -> BenchmarkRanking:

        scores = self._ordenar(
            atributo,
            metrica
        )

        return BenchmarkRanking(scores)
    
    
    