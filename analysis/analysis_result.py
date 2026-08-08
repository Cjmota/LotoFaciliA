from analysis.probability_result import ProbabilityResult

from dataclasses import dataclass, field

from analysis.statistics_result import StatisticsResult

from analysis.markov_result import MarkovResult


@dataclass(slots=True)
class AnalysisResult:

    probability: ProbabilityResult = field(
        default_factory=ProbabilityResult
    )

    statistics: StatisticsResult = field(
        default_factory=StatisticsResult
    )

    bayes: dict = field(
        default_factory=dict
    )

    markov: MarkovResult = field(
        default_factory=MarkovResult
    )

    score: dict = field(
        default_factory=dict
    )
   