from dataclasses import dataclass

from analysis.feature_metadata import FeatureMetadata
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
            "posterior": metadata.get(
                FeatureMetadata.BAYES
            )
        }

    def _score(
        self,
        metadata: dict
    ) -> dict:

        return {
            "final": metadata.get(
                FeatureMetadata.SCORE
            )
        }

    def _markov(
        self,
        metadata: dict
    ) -> MarkovResult:

        return MarkovResult(
            soma=metadata.get(
                FeatureMetadata.MARKOV_SOMA
            )
        )

    def _probability(
        self,
        metadata: dict
    ) -> ProbabilityResult:

        return ProbabilityResult(

            soma=metadata.get(FeatureMetadata.PROB_SOMA),
            pares=metadata.get(FeatureMetadata.PROB_PARES),
            impares=metadata.get(FeatureMetadata.PROB_IMPARES),
            consecutivos=metadata.get(FeatureMetadata.PROB_CONSECUTIVOS),
            linhas=metadata.get(FeatureMetadata.PROB_LINHAS),
            colunas=metadata.get(FeatureMetadata.PROB_COLUNAS)

        )
    
    def _statistics(
        self,
        metadata: dict
    ) -> StatisticsResult:

        return StatisticsResult(

            soma=metadata.get(
                FeatureMetadata.ZSCORE_SOMA
            ),

            pares=metadata.get(
                FeatureMetadata.ZSCORE_PARES
            ),

            impares=metadata.get(
                FeatureMetadata.ZSCORE_IMPARES
            ),

            consecutivos=metadata.get(
                FeatureMetadata.ZSCORE_CONSECUTIVOS
            )

        )