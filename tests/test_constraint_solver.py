from engine.constraint_solver import ConstraintSolver
from engine.template_parser import GameTemplate
from modelos.lottery_set import LotterySet


def test_constraint_solver():

    solver = ConstraintSolver()

    jogo = [
        1,3,5,7,9,
        11,13,15,
        17,19,
        2,4,6,8,10
    ]

    lottery_original = LotterySet(jogo)

    template = GameTemplate(
        pares=8,
        primos=6,
        centro=5,
        fibonacci=4,
        multiplos3=5
    )

    novo = solver.resolver(
        jogo,
        template
    )

    lottery_resultado = LotterySet(novo)

    assert lottery_resultado.pares == 8
    assert lottery_resultado.primos == 6
    assert lottery_resultado.centro == 5
    assert lottery_resultado.fibonacci == 4
    assert lottery_resultado.multiplos3 == 5

