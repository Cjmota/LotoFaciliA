from abc import ABC, abstractmethod

from estimators.weight_estimator import WeightEstimator
from modelos.lottery_set import LotterySet
from modelos.weight import Weight


class CriterionEvaluator(ABC):

    def __init__(self, estimator: WeightEstimator):
        self._estimator = estimator

    @property
    @abstractmethod
    def nome(self) -> str:
        ...

    @property
    @abstractmethod
    def atributo(self) -> str:
        ...

    def avaliar(
        self,
        jogo: LotterySet
    ) -> Weight:

        valor = getattr(
            jogo,
            self.atributo
        )

        return self._estimator.resolver(
            categoria=self.nome,
            valor=valor
        )