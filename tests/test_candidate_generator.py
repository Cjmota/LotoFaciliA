from generator.candidate_generator import CandidateGenerator

from modelos.lottery_set import LotterySet


def test_deve_gerar_uma_combinacao():
    generator = CandidateGenerator()

    jogo = generator.gerar()

    assert len(jogo) == 15

    assert len(set(jogo)) == 15

    assert all(
        1 <= numero <= 25
        for numero in jogo
    )


def test_deve_gerar_combinacoes_diferentes():
    generator = CandidateGenerator()

    jogos = generator.gerar_lote(10)

    assert len(jogos) == 10

    assert len({
        tuple(jogo)
        for jogo in jogos
    }) == 10

def test_deve_gerar_lottery_set():

    generator = CandidateGenerator()

    jogo = generator.gerar()

    assert isinstance(
        jogo,
        LotterySet
    )

    assert jogo.quantidade == 15

    assert len(jogo.estatisticas) > 0

