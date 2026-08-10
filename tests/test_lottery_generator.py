from generator.candidate_generator import CandidateGenerator
from generator.candidate_evaluator import CandidateEvaluator
from generator.candidate_selector import CandidateSelector
from generator.candidate_pipeline import CandidatePipeline
from generator.lottery_generator import LotteryGenerator

from evaluators.pair_criterion_evaluator import PairCriterionEvaluator
from evaluators.prime_criterion_evaluator import PrimeCriterionEvaluator
from evaluators.low_criterion_evaluator import LowCriterionEvaluator
from evaluators.high_criterion_evaluator import HighCriterionEvaluator
from evaluators.center_criterion_evaluator import CenterCriterionEvaluator
from evaluators.border_criterion_evaluator import BorderCriterionEvaluator

from repositories.weight_repository import WeightRepository
from estimators.weight_estimator import WeightEstimator

from modelos.lottery_set import LotterySet


def criar_pipeline():

    repository = WeightRepository()
    estimator = WeightEstimator(repository)

    evaluator = CandidateEvaluator([
        PairCriterionEvaluator(estimator),
        PrimeCriterionEvaluator(estimator),
        LowCriterionEvaluator(estimator),
        HighCriterionEvaluator(estimator),
        CenterCriterionEvaluator(estimator),
        BorderCriterionEvaluator(estimator),
    ])

    generator = CandidateGenerator()
    selector = CandidateSelector()

    return CandidatePipeline(
        generator=generator,
        evaluator=evaluator,
        selector=selector
    )


def test_deve_gerar_jogos_finais():

    pipeline = criar_pipeline()

    generator = LotteryGenerator(
        pipeline
    )

    jogos = generator.gerar(
        quantidade=100,
        melhores=10
    )

    assert len(jogos) == 10

    assert all(
        isinstance(jogo, LotterySet)
        for jogo in jogos
    )

    assert all(
        jogo.quantidade == 15
        for jogo in jogos
    )
    
    jogos = generator.gerar(
        quantidade=100,
        melhores=20
    )

    assert len(jogos) == 20
