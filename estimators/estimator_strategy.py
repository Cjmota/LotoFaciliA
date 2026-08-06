# estimators/estimator_strategy.py

from abc import ABC, abstractmethod

from modelos.weight import Weight


class EstimatorStrategy(ABC):

    def __init__(self):

        self._ultimo_valor = None
        self._ultimo_vizinho = None
        self._ultima_distancia = None

    @abstractmethod
    def estimar(
        self,
        repository,
        categoria,
        valor
    ) -> Weight:
        ...

    @property
    def ultimo_vizinho(self):
        return self._ultimo_vizinho

    @property
    def ultimo_valor(self):
        return self._ultimo_valor

    @property
    def ultima_distancia(self):
        return self._ultima_distancia