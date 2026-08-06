from generator.candidate_evaluator import CandidateEvaluator

from evaluators.pair_criterion_evaluator import PairCriterionEvaluator
from evaluators.prime_criterion_evaluator import PrimeCriterionEvaluator
from evaluators.low_criterion_evaluator import LowCriterionEvaluator
from evaluators.high_criterion_evaluator import HighCriterionEvaluator
from evaluators.center_criterion_evaluator import CenterCriterionEvaluator
from evaluators.border_criterion_evaluator import BorderCriterionEvaluator

from repositories.weight_repository import WeightRepository
from estimators.weight_estimator import WeightEstimator

from modelos.lottery_set import LotterySet


def test_candidate_evaluator():

    repo = WeightRepository()

    estimator = WeightEstimator(repo)

    evaluator = CandidateEvaluator(
        [
            PairCriterionEvaluator(estimator),
            PrimeCriterionEvaluator(estimator),
            LowCriterionEvaluator(estimator),
            HighCriterionEvaluator(estimator),
            CenterCriterionEvaluator(estimator),
            BorderCriterionEvaluator(estimator),
        ]
    )

    jogo = LotterySet(
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    )

    candidate = evaluator.avaliar(jogo)

    print(jogo.baixas)
    print(jogo.altas)

    print(candidate.score.peso("Baixas"))
    print(candidate.score.peso("Altas"))

    assert candidate.existe

    assert len(candidate.score) == 6

    assert candidate.score.total_criterios == 6

    assert candidate.score.peso("Pares").existe
    assert candidate.score.peso("Primos").existe
    assert candidate.score.peso("Baixas").existe
    assert candidate.score.peso("Altas").existe
    assert candidate.score.peso("Centro").existe
    assert candidate.score.peso("Moldura").existe