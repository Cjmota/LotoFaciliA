from dataclasses import dataclass

@dataclass(slots=True)
class BenchmarkStanding:

    estrategia: str

    pontos: int

    vitorias: int = 0

    segundos: int = 0

    terceiros: int = 0

    participacoes: int = 0