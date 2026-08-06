from evaluators.criterion_evaluator import CriterionEvaluator
from modelos.lottery_set import LotterySet
from modelos.weight import Weight


class PairCriterionEvaluator(CriterionEvaluator):

    @property
    def nome(self):
        return "Pares"

    @property
    def atributo(self):
        return "pares"