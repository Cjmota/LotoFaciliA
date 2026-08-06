from analysis.feature import Feature

from domain.concurso import Concurso


class FeatureExtractor:

    def extrair(
        self,
        concurso: Concurso
    ) -> Feature:

        return Feature(

            soma=concurso.soma(),

            pares=concurso.pares(),

            impares=concurso.impares(),

            consecutivos=concurso.consecutivos(),

            linhas=concurso.linhas(),

            colunas=concurso.colunas()

        )

