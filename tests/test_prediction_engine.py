from datetime import date

from analysis.analysis_builder import AnalysisBuilder
from analysis.analysis_pipeline import AnalysisPipeline
from analysis.prediction import Prediction
from analysis.prediction_engine import PredictionEngine
from domain.concurso import Concurso
from domain.historico import Historico


def test_deve_predizer():

    historico = Historico([])

    pipeline = AnalysisPipeline.default(
        historico
    )

    engine = PredictionEngine(

        pipeline,

        AnalysisBuilder()

    )

    concurso = Concurso(
        numero=1,
        data=date(2026, 1, 1),
        dezenas=frozenset(range(1, 16))
    )

    prediction = engine.predict(
        concurso
    )

    assert isinstance(
        prediction,
        Prediction
    )

    assert prediction.feature.soma == 120