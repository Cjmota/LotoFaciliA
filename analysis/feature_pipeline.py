from dataclasses import dataclass, field

from analysis.feature import Feature
from analysis.feature_stage import FeatureStage


@dataclass(slots=True)
class FeaturePipeline:

    stages: list[FeatureStage] = field(default_factory=list)

    def processar(
        self,
        feature: Feature
    ) -> Feature:

        for stage in self.stages:

            feature = stage.processar(feature)

        return feature
