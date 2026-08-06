
from dataclasses import dataclass, field

from modelos.weight import Weight


@dataclass(frozen=True)
class CandidateScore:

    avaliacoes: dict[str, Weight] = field(default_factory=dict)
    
    def __len__(self):
        return len(self.avaliacoes)
    
    def __lt__(self, other: "CandidateScore") -> bool:
        return self.score_total < other.score_total
    
    @property
    def vazio(self) -> bool:
        return self.score_total == 0
    
    @property
    def existe(self) -> bool:
        return self.score_total > 0
    
    def peso(self, criterio: str) -> Weight:

        return self.avaliacoes.get(
            criterio,
            Weight()
        )
        
    @property
    def total_criterios(self) -> int:

        return len(self.avaliacoes)
    
    @property
    def nota_media(self) -> float:

        if not self.avaliacoes:
            return 0.0

        return (
            sum(
                peso.score_base
                for peso in self.avaliacoes.values()
            )
            / len(self.avaliacoes)
        )
    
    @property
    def score_total(self) -> float:

        if not self.avaliacoes:
            return 0.0

        return sum(
            peso.score_base
            for peso in self.avaliacoes.values()
        )
        
    @property
    def confianca(self) -> float:

        if not self.avaliacoes:
            return 0.0

        return sum(
            peso.confianca
            for peso in self.avaliacoes.values()
        ) / len(self.avaliacoes)
    
    
    