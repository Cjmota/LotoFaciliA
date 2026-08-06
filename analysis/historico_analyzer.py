from dataclasses import dataclass

from domain.historico import Historico

from collections import Counter


@dataclass(slots=True)
class HistoricoAnalyzer:

    historico: Historico
    
    
    def frequencia(
        self,
        dezena: int
    ) -> int:

        return sum(

            1

            for concurso in self.historico

            if concurso.contem(dezena)

        )
    
    def frequencias(self) -> dict[int, int]:

        return {

            dezena: self.frequencia(dezena)

            for dezena in range(1, 26)

        }

    def _distribuicao(
        self,
        extrator
    ) -> dict:

        return dict(

            Counter(

                extrator(concurso)

                for concurso in self.historico

            )

        )
    
    def distribuicao_somas(self):

        return self._distribuicao(

            lambda concurso: concurso.soma()

        )
    
    def distribuicao_pares(self):

        return self._distribuicao(

            lambda concurso: concurso.pares()

        )
    
    def distribuicao_impares(self):

        return self._distribuicao(

            lambda concurso: concurso.impares()

        )
    
    def distribuicao_consecutivos(self):

        return self._distribuicao(

            lambda concurso: concurso.consecutivos()

        )
    
    def distribuicao_linhas(self):

        return self._distribuicao(

            lambda concurso: concurso.linhas()

        )
    
    def distribuicao_colunas(self):

        return self._distribuicao(

            lambda concurso: concurso.colunas()

        )
    
    
    