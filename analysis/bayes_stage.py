from dataclasses import dataclass

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

            "prob_soma",

            "prob_pares",

            "prob_impares",

            "prob_consecutivos"

        ):

            if chave in metadata:

                evidencias.append(

                    BayesEvidence(

                        metadata[chave]

                    )

                )

        priori = metadata.get(

            "score",

            1.0

        )

        metadata["bayes"] = self.bayes.posterior(

            priori=priori,

            evidencias=evidencias

        )

        return self.atualizar(
            feature,
            metadata
        )
    
    