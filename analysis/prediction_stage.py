from abc import ABC
from abc import abstractmethod

from analysis.prediction import Prediction


class PredictionStage(ABC):

    @abstractmethod
    def processar(
        self,
        prediction: Prediction
    ) -> Prediction:
        ...