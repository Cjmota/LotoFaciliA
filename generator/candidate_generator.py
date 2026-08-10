import random
from modelos.lottery_set import LotterySet


class CandidateGenerator:

    def gerar(self):

        return LotterySet(
            random.sample(
                range(1, 26),
                15
            )
        )

    def gerar_lote(
        self,
        quantidade
    ):

        jogos = set()

        while len(jogos) < quantidade:

            jogo = self.gerar()

            jogos.add(jogo)

        return list(jogos)
            