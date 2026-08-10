from evaluators.criterion_evaluator import CriterionEvaluator

class LineCriterionEvaluator(CriterionEvaluator):

    @property
    def nome(self):
        return "Linhas"

    @property
    def atributo(self):
        return "linhas"
