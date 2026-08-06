from dataclasses import dataclass


@dataclass
class ConstraintError:
    atributo: str
    esperado: object
    encontrado: object
    diferenca: object = None

    def __str__(self):
        return (
            f"{self.atributo}: "
            f"{self.encontrado} -> "
            f"{self.esperado}"
        )