from dataclasses import fields

from modelos.weight import Weight


class WeightInterpolator:

    def interpolar(
        self,
        valor_inferior: int,
        peso_inferior: Weight,
        valor_superior: int,
        peso_superior: Weight,
        valor_procurado: int,
    ) -> Weight:

        if valor_inferior == valor_superior:
            return peso_inferior

        fator = self._calcular_fator(
            valor_inferior,
            valor_superior,
            valor_procurado,
        )

        dados = {}

        for campo in fields(Weight):

            valor1 = getattr(peso_inferior, campo.name)
            valor2 = getattr(peso_superior, campo.name)

            valor = self._lerp(
                valor1,
                valor2,
                fator,
            )

            if campo.type is int:
                valor = round(valor)

            dados[campo.name] = valor

        return Weight(**dados)

    @staticmethod
    def _calcular_fator(
        inferior: int,
        superior: int,
        procurado: int,
    ) -> float:

        return (
            procurado - inferior
        ) / (
            superior - inferior
        )

    @staticmethod
    def _lerp(
        a: float,
        b: float,
        t: float,
    ):

        return a + (b - a) * t