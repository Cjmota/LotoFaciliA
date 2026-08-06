from collections.abc import Callable
from dataclasses import dataclass

from analysis.feature import Feature
from analysis.markov_chain import MarkovChain
from analysis.metadata_stage import MetadataStage

@dataclass(slots=True)
class MarkovStage(MetadataStage):

    cadeia: MarkovChain

    extrator: Callable[[Feature], object]

    nome_metadata: str
    
    def processar(
        self,
        feature: Feature
    ) -> Feature:

        metadata = dict(

            feature.metadata

        )

        estado = self.extrator(

            feature

        )

        proximo = self.cadeia.prever_proximo_estado(

            estado

        )

        if proximo is None:

            metadata[self.nome_metadata] = 0

        else:

            metadata[self.nome_metadata] = (

                self.cadeia.probabilidade(

                    estado,

                    proximo

                )

            )

        return self.atualizar(

            feature,

            metadata

        )