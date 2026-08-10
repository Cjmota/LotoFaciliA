from evaluators.criterion_evaluator import CriterionEvaluator

class FibonacciCriterionEvaluator(CriterionEvaluator):

    @property
    def nome(self):
        return "Fibonacci"

    @property
    def atributo(self):
        return "fibonacci"
