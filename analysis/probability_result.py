from dataclasses import dataclass


@dataclass(slots=True)
class ProbabilityResult:

    soma: float | None = None
    pares: float | None = None
    impares: float | None = None
    consecutivos: float | None = None
    linhas: float | None = None
    colunas: float | None = None