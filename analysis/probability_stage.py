from collections.abc import Callable
from dataclasses import dataclass

from analysis.feature import Feature
from analysis.historico_statistics import HistoricoStatistics
from analysis.metadata_stage import MetadataStage


@dataclass(slots=True)
class ProbabilityStage(MetadataStage):

    distribuicao: Callable[[], dict]

    extrator: Callable[[Feature], object]

    nome_metadata: str

    statistics: HistoricoStatistics
    
    def _adicionar_probabilidade(
        self,
        metadata: dict,
        nome: str,
        valor,
        distribuicao
    ) -> None:

        metadata[nome] = self.statistics.probabilidade(
            valor,
            distribuicao
        )

    def processar(
        self,
        feature: Feature
    ) -> Feature:

        metadata = dict(

            feature.metadata

        )

        distribuicao = self.distribuicao()

        valor = self.extrator(

            feature

        )

        metadata[self.nome_metadata] = (

            self.statistics.probabilidade(

                valor,

                distribuicao

            )

        )

        return self.atualizar(

            feature,

            metadata

        )
    
    