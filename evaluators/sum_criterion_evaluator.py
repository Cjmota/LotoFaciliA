from evaluators.criterion_evaluator import CriterionEvaluator

class SumCriterionEvaluator(CriterionEvaluator):

    @property
    def nome(self):
        return "Faixa_Soma"

    @property
    def atributo(self):
        return "faixa_soma"
