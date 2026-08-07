from dataclasses import dataclass, field

from analysis.feature import Feature

from analysis.analysis_result import AnalysisResult


@dataclass(slots=True)
class Prediction:

    feature: Feature

    analysis: AnalysisResult = field(

        default_factory=AnalysisResult

    )