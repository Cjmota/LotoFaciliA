from engine.game import Game

from engine.probability_engine import ProbabilityEngine
from engine.score_engine import ScoreEngine
from engine.validator_engine import ValidatorEngine
from engine.ranking_engine import RankingEngine


class GeneratorEngine:

    def __init__(

        self,

        probability_engine=None,

        score_engine=None,

        validator_engine=None,

        ranking_engine=None

    ):

        self.probability_engine = (

            probability_engine

            or

            ProbabilityEngine()

        )

        self.score_engine = score_engine or ScoreEngine()

        self.validator_engine = (

            validator_engine

            or

            ValidatorEngine()

        )

        self.ranking_engine = (

            ranking_engine

            or

            RankingEngine()

        )
         
    def criar(

        self,

        dezenas: list[int]

    ) -> Game:

        return Game(

            dezenas=dezenas

        )
    
    def calcular_probabilidade(
        self,
        game: Game
    ) -> Game:

        score = self.probability_engine.avaliar(game)

        game.definir_score(score)

        return game
    
    def calcular_score(

        self,

        game: Game

    ) -> Game:

        self._verificar_estado(
        
        game.tem_score,

                "O jogo ainda não possui GameScore."

            )

        self.score_engine.calcular(

            game.score

        )

        return game
    
    def validar(

        self,

        game: Game

    ) -> Game:

        if not game.tem_score:

            raise ValueError(

                "O jogo ainda não foi avaliado."

            )

        valido, erros = self.validator_engine.validar(game)

        game.atualizar_validacao(

            valido,

            erros

        )

        return game
    
    def gerar(

        self,

        dezenas

    ):
        
        game = self.criar(dezenas)

        return self._avaliar(game)
    
    def ranquear(

        self,

        jogos
    ):
        
        return self.ranking_engine.top(

            jogos,

            100

        )
    
    def gerar_lote(

        self,

        lista_de_dezenas,

        quantidade=100

    ):
        
        avaliados = self.avaliar_lote(

            lista_de_dezenas

        )

        return self.ranking_engine.top(

            avaliados,

            quantidade

        )
    
    def avaliar_lote(

        self,

        jogos
    ):
        
        return [

        self._avaliar(

            self.criar(jogo)

        )

        for jogo in jogos

    ]        
    
    def melhores(

        self,

        jogos,

        quantidade=100
    ):
        
        avaliados = self.avaliar_lote(jogos)

        return self.ranking_engine.top(

            avaliados,

            quantidade

        )
        
    def _avaliar(

        self,

        game: Game

    ) -> Game:

        game = self.calcular_probabilidade(game)

        game = self.calcular_score(game)

        game = self.validar(game)

        return game
    
    def avaliar(

        self,

        game: Game

    ) -> Game:

        return self._avaliar(game)
    
    def _verificar_estado(
        
        self,
        
        condicao,
        
        mensagem
        
    ):
        
        if not condicao:
            
            raise ValueError(mensagem)
         
    @property
    def engines(self):

        return (

            self.probability_engine,

            self.score_engine,

            self.validator_engine,

            self.ranking_engine

        )
    
    