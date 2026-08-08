from dataclasses import dataclass

from analysis.analysis_builder import AnalysisBuilder
from analysis.analyzer import Analyzer
from analysis.prediction import Prediction
from domain.concurso import Concurso


@dataclass(slots=True)
class PredictionEngine:

    analyzer: Analyzer
    builder: AnalysisBuilder

    def predict(
        self,
        concurso: Concurso
    ) -> Prediction:

        feature = self.analyzer.analisar(concurso)

        analysis = self.builder.build(
            feature
        )

        return Prediction(
            feature=feature,
            analysis=analysis
        )
    
    
        