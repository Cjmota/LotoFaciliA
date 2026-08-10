from evaluators.fibonacci_criterion_evaluator import FibonacciCriterionEvaluator
from evaluators.multiple3_criterion_evaluator import Multiple3CriterionEvaluator
from evaluators.consecutive_criterion_evaluator import ConsecutiveCriterionEvaluator
from evaluators.sum_criterion_evaluator import SumCriterionEvaluator
from evaluators.line_criterion_evaluator import LineCriterionEvaluator
from evaluators.column_criterion_evaluator import ColumnCriterionEvaluator

from repositories.weight_repository import WeightRepository
from estimators.weight_estimator import WeightEstimator
from modelos.lottery_set import LotterySet


def test_deve_avaliar_os_seis_novos_criterios():

    repository = WeightRepository()
    estimator = WeightEstimator(repository)

    avaliadores = [
        FibonacciCriterionEvaluator(estimator),
        Multiple3CriterionEvaluator(estimator),
        ConsecutiveCriterionEvaluator(estimator),
        SumCriterionEvaluator(estimator),
        LineCriterionEvaluator(estimator),
        ColumnCriterionEvaluator(estimator),
    ]

    jogo = LotterySet(
        [1, 2, 3, 4, 5,
         6, 7, 8, 9, 10,
         11, 12, 13, 14, 15]
    )

    for avaliador in avaliadores:

        peso = avaliador.avaliar(jogo)

        print(
            avaliador.nome,
            avaliador.atributo,
            getattr(jogo, avaliador.atributo),
            peso
        )

        assert peso.existe
