from collections import defaultdict, Counter


class MarkovChain:

    def __init__(self):

        self.transicoes = defaultdict(Counter)

    def registrar_transicao(
        self,
        estado_atual,
        proximo_estado
    ):

        self.transicoes[estado_atual][proximo_estado] += 1

    def probabilidade(
        self,
        estado_atual,
        proximo_estado
    ) -> float:

        contador = self.transicoes[estado_atual]

        total = sum(contador.values())

        if total == 0:
            return 0.0

        return contador[proximo_estado] / total

    def prever_proximo_estado(
        self,
        estado_atual
    ):

        contador = self.transicoes[estado_atual]

        if not contador:
            return None

        return contador.most_common(1)[0][0]