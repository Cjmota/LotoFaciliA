from evaluators.criterion_evaluator import CriterionEvaluator


class ColumnCriterionEvaluator(CriterionEvaluator):

    @property
    def nome(self):
        return "Colunas"

    @property
    def atributo(self):
        return "colunas"
