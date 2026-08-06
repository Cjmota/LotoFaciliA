from dataclasses import dataclass

from benchmarks.benchmark_metrics import BenchmarkMetrics


@dataclass(slots=True)
class BenchmarkReport:

    metricas: dict[str, BenchmarkMetrics]

    @property
    def atributos(self):

        return tuple(self.metricas.keys())

    def obter(self, atributo):

        return self.metricas[atributo]

    def __getitem__(self, atributo):

        return self.metricas[atributo]

    def __contains__(self, atributo):

        return atributo in self.metricas

    def __len__(self):

        return len(self.metricas)

    def __iter__(self):

        return iter(self.metricas.items())
    
    def metrica(
        self,
        atributo: str
    ) -> BenchmarkMetrics:

        return self.metricas[atributo]