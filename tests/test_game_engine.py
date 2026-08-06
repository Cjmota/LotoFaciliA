from engine.game import Game
from engine.game_engine import GameEngine

game = Game(

    dezenas=[
        1,2,3,4,5,
        7,8,9,
        12,13,
        18,
        20,22,24,25
    ]

)

engine = GameEngine()

resultado = engine.avaliar(game)

assert resultado.tem_score
assert resultado.valido in (True, False)
assert resultado.pares == 8