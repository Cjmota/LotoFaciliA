from benchmarks.benchmark_standing import BenchmarkStanding
from dataclasses import dataclass

@dataclass(slots=True)
class BenchmarkTable:
    
    classificacao: list[BenchmarkStanding]
    
    def __post_init__(self):

        self._ordenar(self.classificacao)

    def primeiro(self) -> BenchmarkStanding:

        return self.classificacao[0]

    def ultimo(self) -> BenchmarkStanding:

        return self.classificacao[-1]
    
    def top(self, n: int) -> list[BenchmarkStanding]:

        return self.classificacao[:n]
    
    def bottom(self, n: int) -> list[BenchmarkStanding]:

        return self.classificacao[-n:]

    def obter(
        self,
        estrategia: str
    ) -> BenchmarkStanding:

        for standing in self.classificacao:

            if standing.estrategia == estrategia:
                return standing

        raise KeyError(
            f"Estratégia '{estrategia}' não encontrada."
        )
    
    def _chave_ordenacao(
        self,
        standing: BenchmarkStanding
    ) -> tuple:

        return (
            -standing.pontos,
            -standing.vitorias,
            standing.segundos,
            standing.terceiros,
            standing.estrategia
        ) 
    
    def _ordenar(
        self,
        standings: list[BenchmarkStanding]
    ) -> None:

        standings.sort(
            key=self._chave_ordenacao
        )
    
    def __contains__(
        self,
        estrategia: str
    ):

        return any(

            standing.estrategia == estrategia

            for standing in self.classificacao

        )
        
    def __iter__(self):

        return iter(self.classificacao)
    
    def __len__(self):

        return len(self.classificacao)