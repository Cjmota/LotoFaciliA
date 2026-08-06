from dataclasses import dataclass

from dataclasses import dataclass

from modelos.lottery_set import LotterySet
from generator.candidate_score import CandidateScore


@dataclass(frozen=True)
class Candidate:

    jogo: LotterySet

    score: CandidateScore

    @property
    def score_total(self) -> float:
        return self.score.score_total

    @property
    def confianca(self) -> float:
        return self.score.confianca

    @property
    def vazio(self) -> bool:
        return self.score.vazio

    @property
    def existe(self) -> bool:
        return self.score.existe

    def __lt__(self, other: "Candidate") -> bool:
        return self.score_total < other.score_total

    def __repr__(self) -> str:
        return (
            f"Candidate("
            f"score={self.score_total:.3f}, "
            f"conf={self.confianca:.3f}"
            f")"
        )