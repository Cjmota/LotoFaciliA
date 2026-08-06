from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class FeatureScore:
    """
    Representa a avaliação estatística
    de uma única feature.
    """
    nome: str

    valor: Any

    probabilidade: float = 0.0

    peso_bayes: float = 999.0

    ranking: int = 999

    percentual: float = 0.0

    quantidade: int = 0

    nota: float = 0.0

    observacao: str = ""
    
    def to_dict(self):
        return asdict(self)

    def __str__(self):

        return (
            f"{self.nome:<15}"
            f" Valor={self.valor}"
            f" Prob={self.probabilidade:.4f}"
            f" Peso={self.peso_bayes:.4f}"
            f" Rank={self.ranking}"
        )
    
    @property
    def score(self):

        return (

            self.fator_nota

            *

            self.probabilidade

            *

            self.fator_bayes

            *

            self.fator_ranking

        )

    @property
    def fator_bayes(self):

        if self.peso_bayes <= 0:

            return 1

        return 1 / self.peso_bayes

    @property
    def fator_nota(self):

        return self.nota / 10

    @property
    def fator_ranking(self):

        if self.ranking <= 0:

            return 0

        return 1 / self.ranking
 
    @property
    def existe(self):

        return self.quantidade > 0

    @property
    def raro(self):

        return self.ranking > 20

    @property
    def comum(self):

        return self.ranking <= 5

    @property
    def excelente(self):

        return self.nota >= 9

    