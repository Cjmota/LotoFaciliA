from evaluators.criterion_evaluator import CriterionEvaluator

from generator.candidate import Candidate
from generator.candidate_score import CandidateScore

from modelos.lottery_set import LotterySet


class CandidateEvaluator:

    def __init__(
        self,
        avaliadores: list[CriterionEvaluator]
    ):
        self._avaliadores = tuple(avaliadores)

    def avaliar(
        self,
        jogo: LotterySet
    ) -> Candidate:

        avaliacoes = {

            avaliador.nome: avaliador.avaliar(jogo)

            for avaliador in self._avaliadores

        }

        return Candidate(

            jogo=jogo,

            score=CandidateScore(avaliacoes)

        )