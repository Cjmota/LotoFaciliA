
from weight.default_weight_calculator import DefaultWeightCalculator


class WeightGenerator:

    def __init__(self, statistics, calculator=None):
        self.statistics = statistics
        self.calculator = calculator or DefaultWeightCalculator()
    
    def gerar(self):

        pesos = {}

        resultados = self.statistics.calcular()

        for nome, resultado in resultados.items():

            pesos[nome] = self.gerar_categoria(

                resultado

            )

        return pesos
    
    def gerar_categoria(

        self,

        resultado

    ):

        categoria = {}

        ordenados = sorted(

            resultado.distribuicao.items(),

            key=lambda item: item[1],

            reverse=True

        )

        for ranking, (valor, quantidade) in enumerate(

            ordenados,

            start=1

        ):

            categoria[valor] = self.calculator.calcular(
                quantidade,
                resultado,
                ranking
            )

        return categoria
    
    
  
