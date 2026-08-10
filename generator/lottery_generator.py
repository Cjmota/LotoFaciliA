class LotteryGenerator:

    def __init__(self, pipeline):
        self.pipeline = pipeline

    def gerar(
        self,
        quantidade,
        melhores=10
    ):

        candidatos = self.pipeline.processar(
            quantidade=quantidade,
            melhores=melhores,
        )  

        return [
            candidato.jogo
            for candidato in candidatos
        ]
