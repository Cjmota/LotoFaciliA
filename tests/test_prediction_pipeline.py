from analysis.analysis_result import AnalysisResult
from analysis.feature import Feature
from analysis.prediction import Prediction
from analysis.prediction_pipeline import PredictionPipeline
from analysis.prediction_stage import PredictionStage


class FakePredictionStage(PredictionStage):

    def processar(
        self,
        prediction: Prediction
    ) -> Prediction:

        prediction.analysis.score["teste"] = 1

        return prediction


def test_deve_processar_prediction():

    feature = Feature(

        soma=120,

        pares=7,

        impares=8,

        consecutivos=14,

        linhas=(5, 5, 5, 0, 0),

        colunas=(3, 3, 3, 3, 3)

    )

    prediction = Prediction(

        feature=feature,

        analysis=AnalysisResult()

    )

    pipeline = PredictionPipeline([

        FakePredictionStage()

    ])

    resultado = pipeline.processar(

        prediction

    )

    assert resultado.analysis.score["teste"] == 1