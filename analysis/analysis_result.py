from analysis.probability_result import ProbabilityResult

from dataclasses import dataclass
from dataclasses import field

from analysis.feature import Feature
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
        
    @classmethod
    def _probability(
        cls,
        metadata
    ) -> ProbabilityResult:
        
        return ProbabilityResult(

            soma=metadata.get("prob_soma"),

            pares=metadata.get("prob_pares"),

            impares=metadata.get("prob_impares"),

            consecutivos=metadata.get("prob_consecutivos"),

            linhas=metadata.get("prob_linhas"),

            colunas=metadata.get("prob_colunas")

        )
    
    @classmethod
    def from_feature(
        cls,
        feature: Feature
    ) -> "AnalysisResult":

        return cls.from_metadata(
            feature.metadata
        )
    
    @classmethod
    def _markov(
        cls,
        metadata: dict
    ) -> MarkovResult:

        return MarkovResult(

            soma=metadata.get("markov_soma")

        )
    
    @classmethod
    def _bayes(cls, metadata):

        return {

            "posterior": metadata.get("bayes")

        }
    
    @classmethod
    def _score(cls, metadata):

        return {

            "final": metadata.get("score")

        }
    
    @classmethod
    def from_metadata(
        cls,
        metadata: dict
    ) -> "AnalysisResult":

        return cls(

            probability=cls._probability(metadata),

            statistics=cls._statistics(metadata),

            bayes=cls._bayes(metadata),

            markov=cls._markov(metadata),

            score=cls._score(metadata)

        )
    
    @classmethod
    def _statistics(
        cls,
        metadata: dict
    ) -> StatisticsResult:

        return StatisticsResult(

            soma=metadata.get("zscore_soma"),

            pares=metadata.get("zscore_pares"),

            impares=metadata.get("zscore_impares"),

            consecutivos=metadata.get("zscore_consecutivos")

        )