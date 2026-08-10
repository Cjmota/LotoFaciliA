from generator.candidate_generator import CandidateGenerator
from generator.candidate_evaluator import CandidateEvaluator
from generator.candidate_selector import CandidateSelector
from generator.candidate_pipeline import CandidatePipeline

from evaluators.pair_criterion_evaluator import PairCriterionEvaluator
from evaluators.prime_criterion_evaluator import PrimeCriterionEvaluator
from evaluators.low_criterion_evaluator import LowCriterionEvaluator
from evaluators.high_criterion_evaluator import HighCriterionEvaluator
from evaluators.center_criterion_evaluator import CenterCriterionEvaluator
from evaluators.border_criterion_evaluator import BorderCriterionEvaluator

from repositories.weight_repository import WeightRepository
from estimators.weight_estimator import WeightEstimator

from evaluators.fibonacci_criterion_evaluator import FibonacciCriterionEvaluator
from evaluators.multiple3_criterion_evaluator import Multiple3CriterionEvaluator
from evaluators.consecutive_criterion_evaluator import ConsecutiveCriterionEvaluator
from evaluators.sum_criterion_evaluator import SumCriterionEvaluator
from evaluators.line_criterion_evaluator import LineCriterionEvaluator
from evaluators.column_criterion_evaluator import ColumnCriterionEvaluator


def criar_evaluator():

    repository = WeightRepository()
    estimator = WeightEstimator(repository)

    return CandidateEvaluator([
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
    ])


def test_deve_gerar_avaliar_e_selecionar():

    generator = CandidateGenerator()
    evaluator = criar_evaluator()
    selector = CandidateSelector()

    pipeline = CandidatePipeline(
        generator=generator,
        evaluator=evaluator,
        selector=selector
    )

    resultado = pipeline.processar(
        quantidade=100,
        melhores=10
    )

    assert len(resultado) == 10
    
    assert all(
        len(candidato.score) == 12
        for candidato in resultado
    )

    assert all(
        candidato.existe
        for candidato in resultado
    )

    assert resultado[0].score_total >= resultado[-1].score_total