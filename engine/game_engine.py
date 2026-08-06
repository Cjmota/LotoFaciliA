from engine.validator_engine import ValidatorEngine

from engine.probability_engine import ProbabilityEngine

from engine.score_engine import ScoreEngine

from engine.game import Game

class GameEngine:

    def __init__(self):

        self.validator = ValidatorEngine()
        self.probability = ProbabilityEngine()
        self.score = ScoreEngine()

    def avaliar(self, game: Game):

        ok, erros = self.validator.validar(

            game

        )

        game.atualizar_validacao(

            ok,

            erros

        )

        game_score = self.probability.avaliar(

            game

        )

        game_score = self.score.calcular(

            game_score

        )

        game.definir_score(

            game_score

        )

        return game