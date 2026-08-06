from dataclasses import dataclass
from datetime import date


@dataclass(slots=True, frozen=True)
class Concurso:

    numero: int

    data: date

    dezenas: frozenset[int]
    
    def contem(
        self,
        dezena: int
    ) -> bool:

        return dezena in self.dezenas
    
    def soma(self) -> int:

        return sum(self.dezenas)
    
    def pares(self):

        return self._contar(

            lambda d: d % 2 == 0

        )
    
    def impares(self) -> int:

        return self._contar(

            lambda d: d % 2 != 0

        )
        
    def acertos(
        self,
        dezenas: frozenset[int]
    ) -> int:
        
        return len(self.dezenas & dezenas)
    
    def linhas(self) -> tuple[int, int, int, int, int]:

        linhas = [0] * 5

        for dezena in self.dezenas:

            indice = (dezena - 1) // 5

            linhas[indice] += 1

        return tuple(linhas)
    
    def colunas(self) -> tuple[int, int, int, int, int]:

        colunas = [0] * 5

        for dezena in self.dezenas:

            indice = (dezena - 1) % 5

            colunas[indice] += 1

        return tuple(colunas)

    def consecutivos(self) -> int:

        dezenas = sorted(self.dezenas)

        return sum(

            1

            for atual, proxima in zip(
                dezenas,
                dezenas[1:]
            )

            if proxima == atual + 1

        )
    
    
    
    def _contar(
        self,
        criterio
    ) -> int:

        return sum(

            1

            for dezena in self.dezenas

            if criterio(dezena)

        )
    
    