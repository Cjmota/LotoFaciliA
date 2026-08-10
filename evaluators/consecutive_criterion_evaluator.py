from evaluators.criterion_evaluator import CriterionEvaluator

class ConsecutiveCriterionEvaluator(CriterionEvaluator):

    @property
    def nome(self):
        return "Consecutivos"

    @property
    def atributo(self):
        return "consecutivos"
