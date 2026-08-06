from dataclasses import dataclass

from analysis.feature import Feature
from analysis.metadata_stage import MetadataStage


@dataclass(slots=True)
class ScoreStage(MetadataStage):

    def _calcular_score(
        self,
        metadata: dict
    ) -> float:

        valores = [

            valor

            for valor in metadata.values()

            if isinstance(valor, (int, float))

        ]

        if not valores:

            return 0

        return sum(valores) / len(valores)

    def processar(
        self,
        feature: Feature
    ) -> Feature:

        metadata = dict(feature.metadata)

        metadata["score"] = self._calcular_score(
            metadata
        )

        return self.atualizar(
            feature,
            metadata
        )
