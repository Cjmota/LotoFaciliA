from dataclasses import dataclass

from benchmarks.benchmark_score import BenchmarkScore


@dataclass(slots=True)
class BenchmarkRanking:

    vencedores: list[BenchmarkScore]
    
    def __post_init__(self):

        for posicao, score in enumerate(
            self.vencedores,
            start=1
        ):

            score.posicao = posicao

    def __len__(self) -> int:
        return len(self.vencedores)
    
    def __getitem__(self, indice: int):
        return self.vencedores[indice]
    
    def __iter__(self):
        return iter(self.vencedores)
    
    def __contains__(self, estrategia: str) -> bool:

        return any(

            score.estrategia == estrategia

            for score in self.vencedores

        )
    
    def primeiro(self) -> BenchmarkScore:
        return self.vencedores[0]
    
    def ultimo(self) -> BenchmarkScore:
        return self.vencedores[-1]
    
    def top(self, quantidade: int) -> "BenchmarkRanking":
        
        return BenchmarkRanking(

            self.vencedores[:quantidade]

        )
        
    def bottom(self, quantidade: int) -> "BenchmarkRanking":

        return BenchmarkRanking(
            
            self.vencedores[-quantidade:]
            
        )
        
    def estrategias(self) -> tuple[str, ...]:
        
        return tuple(
            score.estrategia
            for score in self.vencedores
        )
    
    def valores(self) -> tuple[float, ...]:

        return tuple(

            score.valor

            for score in self.vencedores

        )
    
    def obter(self, estrategia: str) -> BenchmarkScore:

        for score in self.vencedores:

            if score.estrategia == estrategia:

                return score

        raise KeyError(
            f"Estratégia '{estrategia}' não encontrada."
        )
        
    