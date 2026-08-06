from evaluators.criterion_evaluator import CriterionEvaluator

from modelos.lottery_set import LotterySet
from modelos.weight import Weight


class CenterCriterionEvaluator(CriterionEvaluator):

    @property
    def nome(self):
        return "Centro"

    @property
    def atributo(self):
        return "centro"