from evaluators.criterion_evaluator import CriterionEvaluator

from modelos.lottery_set import LotterySet
from modelos.weight import Weight


class BorderCriterionEvaluator(CriterionEvaluator):

    @property
    def nome(self):
        return "Moldura"

    @property
    def atributo(self):
        return "moldura"