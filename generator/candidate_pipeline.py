class CandidatePipeline:

    def __init__(
        self,
        generator,
        evaluator,
        selector
    ):
        self.generator = generator
        self.evaluator = evaluator
        self.selector = selector

    def processar(
        self,
        quantidade,
        melhores=10
    ):

        jogos = self.generator.gerar_lote(
            quantidade
        )

        candidatos = [
            self.evaluator.avaliar(jogo)
            for jogo in jogos
        ]

        return self.selector.melhores(
            candidatos,
            melhores
        )