from analysis.feature_extractor import FeatureExtractor
from analysis.feature_pipeline import FeaturePipeline
from domain.concurso import Concurso
from analysis.feature import Feature
from datetime import date


def test_deve_criar_feature():

    feature = Feature(

        soma=180,

        pares=8,

        impares=7,

        consecutivos=3,

        linhas=(3, 3, 3, 3, 3),

        colunas=(2, 4, 3, 3, 3)

    )

    assert feature.soma == 180

    assert feature.pares == 8

    assert feature.impares == 7

    assert feature.consecutivos == 3

    assert feature.linhas == (

        3, 3, 3, 3, 3

    )

    assert feature.colunas == (

        2, 4, 3, 3, 3

    )
    
def test_deve_extrair_features():

    concurso = Concurso(

        numero=1,

        data=date(2026,1,1),

        dezenas=frozenset({

            1,2,3,4,5,
            6,7,8,9,10,
            11,12,13,14,15

        })

    )

    extractor = FeatureExtractor()

    feature = extractor.extrair(concurso)

    assert feature.soma == 120

    assert feature.pares == 7

    assert feature.impares == 8

    assert feature.consecutivos == 14

    assert feature.linhas == (

        5,5,5,0,0

    )

    assert feature.colunas == (

        3,3,3,3,3

    )

def test_deve_criar_feature_com_metadata():

    feature = Feature(

        soma=180,

        pares=8,

        impares=7,

        consecutivos=3,

        linhas=(3,3,3,3,3),

        colunas=(2,4,3,3,3)

    )

    assert feature.metadata == {}
    
