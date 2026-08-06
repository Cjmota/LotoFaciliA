from typing import Protocol

from analysis.feature import Feature


class FeatureStage(Protocol):

    def processar(
        self,
        feature: Feature
    ) -> Feature:
        ...