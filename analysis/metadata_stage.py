from dataclasses import replace

from analysis.feature import Feature
from analysis.feature_stage import FeatureStage


class MetadataStage(FeatureStage):

    def atualizar(
        self,
        feature: Feature,
        metadata: dict
    ) -> Feature:

        return replace(

            feature,

            metadata=metadata

        )