from dataclasses import dataclass

@dataclass(slots=True)
class BenchmarkScore:

    estrategia: str

    atributo: str

    metrica: str

    valor: float

    posicao: int | None = None