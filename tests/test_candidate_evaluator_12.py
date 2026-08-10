from generator.candidate_evaluator import CandidateEvaluator

from evaluators.pair_criterion_evaluator import PairCriterionEvaluator
from evaluators.prime_criterion_evaluator import PrimeCriterionEvaluator
from evaluators.low_criterion_evaluator import LowCriterionEvaluator
from evaluators.high_criterion_evaluator import HighCriterionEvaluator
from evaluators.center_criterion_evaluator import CenterCriterionEvaluator
from evaluators.border_criterion_evaluator import BorderCriterionEvaluator

from evaluators.fibonacci_criterion_evaluator import FibonacciCriterionEvaluator
from evaluators.multiple3_criterion_evaluator import Multiple3CriterionEvaluator
from evaluators.consecutive_criterion_evaluator import ConsecutiveCriterionEvaluator
from evaluators.sum_criterion_evaluator import SumCriterionEvaluator
from evaluators.line_criterion_evaluator import LineCriterionEvaluator
from evaluators.column_criterion_evaluator import ColumnCriterionEvaluator

from repositories.weight_repository import WeightRepository
from estimators.weight_estimator import WeightEstimator
from modelos.lottery_set import LotterySet


def test_deve_avaliar_os_12_criterios():

    repo = WeightRepository()
    estimator = WeightEstimator(repo)

    avaliadores = [
        PairCriterionEvaluator(estimator),
        PrimeCriterionEvaluator(estimator),
        LowCriterionEvaluator(estimator),
        HighCriterionEvaluator(estimator),
        CenterCriterionEvaluator(estimator),
        BorderCriterionEvaluator(estimator),

        FibonacciCriterionEvaluator(estimator),
        Multiple3CriterionEvaluator(estimator),
        ConsecutiveCriterionEvaluator(estimator),
        SumCriterionEvaluator(estimator),
        LineCriterionEvaluator(estimator),
        ColumnCriterionEvaluator(estimator),
    ]

    evaluator = CandidateEvaluator(avaliadores)

    jogo = LotterySet(
        [
            1, 2, 3, 4, 5,
            6, 7, 8, 9, 10,
            11, 12, 13, 14, 15
        ]
    )

    candidato = evaluator.avaliar(jogo)

    assert candidato.existe

    assert len(candidato.score) == 12

    assert candidato.score.total_criterios == 12

    criterios = [
        "Pares",
        "Primos",
        "Baixas",
        "Altas",
        "Centro",
        "Moldura",
        "Fibonacci",
        "Multiplos3",
        "Consecutivos",
        "Faixa_Soma",
        "Linhas",
        "Colunas",
    ]

    for criterio in criterios:

        assert candidato.score.peso(
            criterio
        ).existe
