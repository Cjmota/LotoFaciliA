from engine.probability_repository import ProbabilityRepository
from modelos.lottery_set import LotterySet
from modelos.weight import Weight

from modelos.feature_score import FeatureScore
from modelos.game_score import GameScore

class ProbabilityEngine:

    def __init__(

        self,

        repository=None

    ):

        self.repository = repository or ProbabilityRepository()
   
    def avaliar_item(

        self,

        categoria,

        valor

    ):

        peso = self.repository.consultar(

            categoria,

            valor

        )

        if peso is None:

            return FeatureScore(

                nome=categoria,

                valor=valor

            )
        
        return self._criar_score(

            categoria,

            valor,
            
            peso

        )

    def avaliar(

        self,

        jogo

    ) -> GameScore:

        game_score = GameScore()

        for categoria, valor in jogo.estatisticas_probabilidade.items():

            if isinstance(valor, tuple):

                valor = str(valor)

            game_score.adicionar(

                self.avaliar_item(

                    categoria,

                    valor

                )

            )

        return game_score

    def _criar_score(

        self,

        categoria,

        valor,

        peso: Weight

    ) -> FeatureScore:

        return FeatureScore(

            nome=categoria,

            valor=valor,

            probabilidade=peso.probabilidade,

            peso_bayes=peso.peso_bayes,

            ranking=peso.ranking,

            percentual=peso.percentual,

            quantidade=peso.quantidade,

            nota=peso.nota

        )

if __name__ == "__main__":

    prob = ProbabilityEngine()
