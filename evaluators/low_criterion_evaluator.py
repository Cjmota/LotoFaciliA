from evaluators.criterion_evaluator import CriterionEvaluator

from modelos.lottery_set import LotterySet
from modelos.weight import Weight


class LowCriterionEvaluator(CriterionEvaluator):

    @property
    def nome(self):
        return "Baixas"

    @property
    def atributo(self):
        return "baixas"