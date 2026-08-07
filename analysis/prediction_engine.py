from dataclasses import dataclass

from altair import Feature

from analysis import analysis_result
from analysis.analysis_result import AnalysisResult
from analysis.analyzer import Analyzer
from analysis.prediction import Prediction
from domain.concurso import Concurso


@dataclass(slots=True)
class PredictionEngine:

    analyzer: Analyzer

    def predict(
        self,
        concurso: Concurso
    ) -> Prediction:

        feature = self.analyzer.analisar(concurso)

        analysis = AnalysisResult.from_feature(
            feature
        )
        
        return Prediction(
        
            feature=feature,

            analysis=analysis

        )
    
    def _analysis_result(
        self,
        feature: Feature
    ) -> AnalysisResult:
        
        return AnalysisResult.from_feature(feature)
        
        