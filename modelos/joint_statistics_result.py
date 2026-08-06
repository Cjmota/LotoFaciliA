
from dataclasses import dataclass


@dataclass(frozen=True)
class JointStatisticsResult:

    atributos: tuple[str, ...]

    distribuicao: dict[tuple, int]

    @property
    def total(self):
        return sum(self.distribuicao.values())

    @property
    def frequencia_maxima(self):
        return max(self.distribuicao.values())

    @property
    def quantidade_combinacoes(self):
        return len(self.distribuicao)

    def frequencia(self, chave: tuple):
        return self.distribuicao.get(chave, 0)