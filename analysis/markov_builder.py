from collections.abc import Callable

from analysis.markov_chain import MarkovChain
from domain.concurso import Concurso
from domain.historico import Historico


class MarkovBuilder:

    def construir(
        self,
        historico: Historico,
        extrator: Callable[[Concurso], object]
    ) -> MarkovChain:

        cadeia = MarkovChain()

        concursos = list(historico)

        for atual, proximo in zip(

            concursos,

            concursos[1:]

        ):

            cadeia.registrar_transicao(

                extrator(atual),

                extrator(proximo)

            )

        return cadeia

    def construir_somas(
        self,
        historico: Historico
    ) -> MarkovChain:

        return self.construir(

            historico,

            lambda concurso: concurso.soma()

        )

    def construir_pares(
        self,
        historico: Historico
    ) -> MarkovChain:

        return self.construir(

            historico,

            lambda concurso: concurso.pares()

        )

    def construir_impares(
        self,
        historico: Historico
    ) -> MarkovChain:

        return self.construir(

            historico,

            lambda concurso: concurso.impares()

        )

    def construir_consecutivos(
        self,
        historico: Historico
    ) -> MarkovChain:

        return self.construir(

            historico,

            lambda concurso: concurso.consecutivos()

        )

    def construir_linhas(
        self,
        historico: Historico
    ) -> MarkovChain:

        return self.construir(

            historico,

            lambda concurso: concurso.linhas()

        )

    def construir_colunas(
        self,
        historico: Historico
    ) -> MarkovChain:

        return self.construir(

            historico,

            lambda concurso: concurso.colunas()

        )