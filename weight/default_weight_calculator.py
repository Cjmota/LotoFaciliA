from modelos.weight import Weight
from weight.weight_calculator import WeightCalculator


class DefaultWeightCalculator(WeightCalculator):

    def calcular(
        self,
        quantidade,
        resultado,
        ranking
    ) -> Weight:

        probabilidade = quantidade / resultado.total

        percentual = probabilidade * 100

        peso_bayes = probabilidade

        nota = round(
            (quantidade / resultado.frequencia_maxima) * 10,
            2
        )

        return Weight(
            probabilidade=probabilidade,
            peso_bayes=peso_bayes,
            percentual=percentual,
            ranking=ranking,
            quantidade=quantidade,
            nota=nota
        )
    
    
    