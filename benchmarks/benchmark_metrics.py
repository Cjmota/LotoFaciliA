from dataclasses import dataclass


@dataclass(slots=True)
class BenchmarkMetrics:

    atributo: str

    quantidade: int

    mae: float

    rmse: float

    erro_maximo: float

    erro_minimo: float

    mediana: float

    desvio_padrao: float