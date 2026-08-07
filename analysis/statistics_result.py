from dataclasses import dataclass


@dataclass(slots=True)
class StatisticsResult:

    soma: float | None = None

    pares: float | None = None

    impares: float | None = None

    consecutivos: float | None = None