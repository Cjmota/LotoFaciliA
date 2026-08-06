from evaluators.criterion_evaluator import CriterionEvaluator

from modelos.lottery_set import LotterySet
from modelos.weight import Weight


class HighCriterionEvaluator(CriterionEvaluator):

    @property
    def nome(self):
        return "Altas"

    @property
    def atributo(self):
        return "altas"