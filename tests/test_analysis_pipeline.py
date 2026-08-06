from analysis.analysis_pipeline import AnalysisPipeline
from analysis.feature_extractor import FeatureExtractor
from analysis.feature_pipeline import FeaturePipeline
from analysis.metadata_stage import MetadataStage
from domain.historico import Historico
from analysis.feature import Feature
from domain.concurso import Concurso
from datetime import date


class FakeStage(MetadataStage):

    def processar(
        self,
        feature: Feature
    ) -> Feature:

        metadata = dict(feature.metadata)

        metadata["fake"] = True

        return self.atualizar(
            feature,
            metadata
        )

def test_deve_criar_pipeline():

    pipeline = AnalysisPipeline(

        extractor=FeatureExtractor(),

        pipeline=FeaturePipeline([])

    )

    assert pipeline is not None

def test_deve_extrair_feature():

    pipeline = AnalysisPipeline(

        extractor=FeatureExtractor(),

        pipeline=FeaturePipeline([])

    )

    concurso = Concurso(

        numero=1,

        data=date(2026, 1, 1),

        dezenas=frozenset({

            1,2,3,4,5,
            6,7,8,9,10,
            11,12,13,14,15

        })

    )

    feature = pipeline.extrair(concurso)

    assert isinstance(feature, Feature)

    assert feature.soma == 120

    assert feature.pares == 7

def test_deve_processar_pipeline():

    pipeline = AnalysisPipeline(

        extractor=FeatureExtractor(),

        pipeline=FeaturePipeline([

            FakeStage()

        ])

    )

    concurso = Concurso(

        numero=1,

        data=date(2026,1,1),

        dezenas=frozenset(range(1,16))

    )

    feature = pipeline.analisar(concurso)

    assert feature.metadata["fake"] is True

def test_deve_criar_pipeline_padrao():

    historico = Historico([])

    pipeline = AnalysisPipeline.default(

        historico

    )

    assert isinstance(

        pipeline,

        AnalysisPipeline

    )

def test_deve_analisar_concurso():

    historico = Historico([

        Concurso(

            numero=1,

            data=date(2026,1,1),

            dezenas=frozenset(range(1,16))

        ),

        Concurso(

            numero=2,

            data=date(2026,1,2),

            dezenas=frozenset(range(1,16))

        )

    ])

    pipeline = AnalysisPipeline.default(

        historico

    )

    concurso = Concurso(

        numero=3,

        data=date(2026,1,3),

        dezenas=frozenset(range(1,16))

    )

    feature = pipeline.analisar(

        concurso

    )

    assert "prob_soma" in feature.metadata

    assert "zscore_soma" in feature.metadata

    assert "bayes" in feature.metadata

    assert "score" in feature.metadata

