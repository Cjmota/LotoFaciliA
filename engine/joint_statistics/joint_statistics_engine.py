from collections import Counter

from modelos.joint_statistics_result import JointStatisticsResult


class JointStatisticsEngine:

    def __init__(

        self,

        historico,

        atributos: tuple[str, ...]

    ):

        if len(atributos) < 2:

            raise ValueError(

                "Informe pelo menos dois atributos."

            )

        self.historico = historico

        self.atributos = atributos

    def calcular(self):

        distribuicao = Counter()

        for concurso in self.historico:

            chave = tuple(

                getattr(

                    concurso,

                    atributo

                )

                for atributo in self.atributos

            )

            distribuicao[chave] += 1

        distribuicao = dict(

            sorted(

                distribuicao.items()

            )

        )

        return JointStatisticsResult(

            atributos=self.atributos,

            distribuicao=distribuicao

        )