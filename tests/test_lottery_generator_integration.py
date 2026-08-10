from generator.candidate_generator import CandidateGenerator
from generator.candidate_evaluator import CandidateEvaluator
from generator.candidate_selector import CandidateSelector
from generator.candidate_pipeline import CandidatePipeline
from generator.lottery_generator import LotteryGenerator

from engine.generator_engine import GeneratorEngine

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

from engine.game import Game


def criar_lottery_generator():

    repository = WeightRepository()
    estimator = WeightEstimator(repository)

    evaluator = CandidateEvaluator([
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

    pipeline = CandidatePipeline(
        generator=CandidateGenerator(),
        evaluator=evaluator,
        selector=CandidateSelector()
    )

    return LotteryGenerator(pipeline)


def test_lottery_generator_deve_integrar_com_generator_engine():

    lottery_generator = criar_lottery_generator()

    jogos = lottery_generator.gerar(
        quantidade=100,
        melhores=10
    )

    engine = GeneratorEngine()

    games = [
        engine.gerar(jogo.dezenas)
        for jogo in jogos
    ]

    assert len(games) == 10

    assert all(
        isinstance(game, Game)
        for game in games
    )

    assert all(
        game.tem_score
        for game in games
    )

    assert all(
        game.quantidade == 15
        for game in games
    )

    assert all(
        game.valido in (True, False)
        for game in games
    )
