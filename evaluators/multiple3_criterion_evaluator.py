from evaluators.criterion_evaluator import CriterionEvaluator

class Multiple3CriterionEvaluator(CriterionEvaluator):

    @property
    def nome(self):
        return "Multiplos3"

    @property
    def atributo(self):
        return "multiplos3"
