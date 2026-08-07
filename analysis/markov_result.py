from dataclasses import dataclass


@dataclass(slots=True)
class MarkovResult:

    soma: float | None = None