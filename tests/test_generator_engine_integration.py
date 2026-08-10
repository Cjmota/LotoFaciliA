from engine.generator_engine import GeneratorEngine
from engine.game import Game


def test_generator_engine_deve_gerar_um_game():
    generator = GeneratorEngine()

    game = generator.gerar([
        1, 2, 3, 4, 5,
        7, 8, 9,
        12, 13,
        18,
        20, 22, 24, 25
    ])

    assert isinstance(game, Game)

    assert len(game) == 15

    assert game.tem_score

    assert game.valido in (True, False)

    assert game.pares == 8
