from generator.candidate_generator import CandidateGenerator
from generator.candidate_evaluator import CandidateEvaluator
from modelos.weight import Weight


class FakeCriterionEvaluator:

    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def avaliar(self, jogo):

        return Weight(
            probabilidade=0.5,
            nota=self.nota,
            quantidade=1
        )


def test_deve_gerar_e_avaliar_candidato():

    generator = CandidateGenerator()

    evaluator = CandidateEvaluator([
        FakeCriterionEvaluator(
            "Pares",
            10
        ),
        FakeCriterionEvaluator(
            "Baixas",
            8
        )
    ])

    jogo = generator.gerar()

    candidato = evaluator.avaliar(jogo)

    assert candidato.existe

    assert candidato.jogo == jogo

    assert candidato.score.total_criterios == 2

    assert candidato.score.peso("Pares").nota == 10

    assert candidato.score.peso("Baixas").nota == 8