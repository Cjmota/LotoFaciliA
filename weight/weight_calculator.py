from abc import ABC, abstractmethod

from modelos.weight import Weight


class WeightCalculator(ABC):

    @abstractmethod
    def calcular(
        self,
        quantidade,
        resultado,
        ranking
    ) -> Weight:
        ...
    
    