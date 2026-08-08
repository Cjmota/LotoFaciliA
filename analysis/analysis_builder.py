from dataclasses import dataclass

from analysis.analysis_result import AnalysisResult
from analysis.feature import Feature
from analysis.probability_result import ProbabilityResult
from analysis.statistics_result import StatisticsResult

from analysis.markov_result import MarkovResult


@dataclass(slots=True)
class AnalysisBuilder:

    def build(
        self,
        feature: Feature
    ) -> AnalysisResult:

        metadata = feature.metadata

        return AnalysisResult(
            probability=self._probability(metadata),
            statistics=self._statistics(metadata),
            markov=self._markov(metadata),
            bayes=self._bayes(metadata),
            score=self._score(metadata)
        )

    def _bayes(
        self,
        metadata: dict
    ) -> dict:

        return {
            "posterior": metadata.get("bayes")
        }

    def _score(
        self,
        metadata: dict
    ) -> dict:

        return {
            "final": metadata.get("score")
        }

    def _markov(
        self,
        metadata: dict
    ) -> MarkovResult:

        return MarkovResult(
            soma=metadata.get("markov_soma")
        )

    def _probability(
        self,
        metadata: dict
    ) -> ProbabilityResult:

        return ProbabilityResult(

            soma=metadata.get("prob_soma"),

            pares=metadata.get("prob_pares"),

            impares=metadata.get("prob_impares"),

            consecutivos=metadata.get("prob_consecutivos"),

            linhas=metadata.get("prob_linhas"),

            colunas=metadata.get("prob_colunas")

        )
    
    def _statistics(
        self,
        metadata: dict
    ) -> StatisticsResult:

        return StatisticsResult(

            soma=metadata.get("zscore_soma"),

            pares=metadata.get("zscore_pares"),

            impares=metadata.get("zscore_impares"),

            consecutivos=metadata.get("zscore_consecutivos")

        )