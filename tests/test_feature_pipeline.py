from analysis.feature import Feature
from analysis.feature_pipeline import FeaturePipeline


def test_deve_criar_pipeline():

    pipeline = FeaturePipeline()

    feature = Feature(

        soma=180,

        pares=8,

        impares=7,

        consecutivos=3,

        linhas=(3,3,3,3,3),

        colunas=(2,4,3,3,3)

    )

    resultado = pipeline.processar(feature)

    assert resultado is feature