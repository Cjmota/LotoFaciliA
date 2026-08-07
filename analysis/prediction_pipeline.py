from dataclasses import dataclass

from analysis.prediction import Prediction
from analysis.prediction_stage import PredictionStage


@dataclass(slots=True)
class PredictionPipeline:

    stages: list[PredictionStage]

    def processar(
        self,
        prediction: Prediction
    ) -> Prediction:

        for stage in self.stages:

            prediction = stage.processar(
                prediction
            )

        return prediction