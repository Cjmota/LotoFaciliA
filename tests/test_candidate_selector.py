from generator.candidate import Candidate
from generator.candidate_selector import CandidateSelector
from generator.candidate_score import CandidateScore
from modelos.lottery_set import LotterySet
from modelos.weight import Weight


def criar_candidato(dezenas, nota):

    jogo = LotterySet(dezenas)

    score = CandidateScore({
        "Pares": Weight(
            probabilidade=1.0,
            quantidade=1,
            nota=nota
        )
    })

    return Candidate(
        jogo=jogo,
        score=score
    )


def test_deve_selecionar_melhores_candidatos():

    candidatos = [
        criar_candidato(range(2, 17), 9),
        criar_candidato(range(3, 18), 7),
        criar_candidato(range(4, 19), 8),
    ]

    selector = CandidateSelector()

    resultado = selector.melhores(
        candidatos,
        2
    )

    assert len(resultado) == 2
    assert resultado[0].score_total == 9
    assert resultado[1].score_total == 8


def test_deve_retornar_lista_vazia_quando_nao_houver_candidatos():

    selector = CandidateSelector()

    resultado = selector.melhores(
        [],
        10
    )

    assert resultado == []
