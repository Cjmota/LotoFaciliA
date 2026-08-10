from collections.abc import Iterable

from generator.candidate import Candidate


class CandidateSelector:

    def melhores(
        self,
        candidatos: Iterable[Candidate],
        quantidade: int = 10
    ) -> list[Candidate]:

        return sorted(
            candidatos,
            reverse=True
        )[:quantidade]
