from dataclasses import dataclass
from analysis.feature_metadata import FeatureMetadata
from analysis.bayes import Bayes
from analysis.bayes_evidence import BayesEvidence
from analysis.feature import Feature
from analysis.metadata_stage import MetadataStage


@dataclass(slots=True)
class BayesStage(MetadataStage):

    bayes: Bayes

    def processar(
        self,
        feature: Feature
    ) -> Feature:

        metadata = dict(feature.metadata)

        evidencias = []

        for chave in (

            FeatureMetadata.PROB_SOMA,

            FeatureMetadata.PROB_PARES,

            FeatureMetadata.PROB_IMPARES,

            FeatureMetadata.PROB_CONSECUTIVOS

        ):

            if chave in metadata:

                evidencias.append(

                    BayesEvidence(

                        metadata[chave]

                    )

                )

        priori = metadata.get(
            FeatureMetadata.SCORE,
            1.0
        )

        metadata[FeatureMetadata.BAYES] = self.bayes.posterior(

            priori=priori,

            evidencias=evidencias

        )

        return self.atualizar(
            feature,
            metadata
        )
    
    