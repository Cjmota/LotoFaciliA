from dataclasses import dataclass
from analysis.feature import Feature
from analysis.historico_statistics import HistoricoStatistics
from analysis.metadata_stage import MetadataStage
from collections.abc import Callable

@dataclass(slots=True)
class StatisticsStage(MetadataStage):

    distribuicao: Callable[[], dict]

    extrator: Callable[[Feature], object]

    nome_metadata: str

    statistics: HistoricoStatistics

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

            self.statistics.zscore(

                valor,

                distribuicao

            )

        )

        return self.atualizar(

            feature,

            metadata

        )
    
    