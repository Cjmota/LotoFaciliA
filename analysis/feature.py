from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True)
class Feature:

    soma: int

    pares: int

    impares: int

    consecutivos: int

    linhas: tuple[int, ...]

    colunas: tuple[int, ...]

    metadata: dict[str, float] = field(

        default_factory=dict

    )
