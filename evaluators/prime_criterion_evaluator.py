from evaluators.criterion_evaluator import CriterionEvaluator

from modelos.lottery_set import LotterySet
from modelos.weight import Weight


class PrimeCriterionEvaluator(CriterionEvaluator):

    @property
    def nome(self) -> str:
        return "Primos"

    @property
    def atributo(self):
        return "primos"