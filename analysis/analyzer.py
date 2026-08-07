from abc import ABC
from abc import abstractmethod

from analysis.feature import Feature
from domain.concurso import Concurso


class Analyzer(ABC):

    @abstractmethod
    def analisar(
        self,
        concurso: Concurso
    ) -> Feature:
        ...