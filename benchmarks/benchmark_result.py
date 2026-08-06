from dataclasses import dataclass

from modelos.weight import Weight


@dataclass(slots=True)
class BenchmarkResult:

    categoria: str
    valor: int

    real: Weight
    estimado: Weight
    
    erro_nota: float = 0.0
    erro_probabilidade: float = 0.0

    tempo_execucao: float = 0.0

    estrategia: str = ""

