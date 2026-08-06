from analysis.historico_statistics import HistoricoStatistics
from analysis.markov_builder import MarkovBuilder
from analysis.markov_stage import MarkovStage
from analysis.probability_stage import ProbabilityStage
from analysis.historico_analyzer import HistoricoAnalyzer
from analysis.feature_extractor import FeatureExtractor
from analysis.feature_pipeline import FeaturePipeline
from analysis.statistics_stage import StatisticsStage
from analysis.score_stage import ScoreStage
from analysis.bayes_stage import BayesStage
from collections.abc import Callable
from domain.historico import Historico
from domain.concurso import Concurso
from dataclasses import dataclass
from analysis.bayes import Bayes
from operator import attrgetter


@dataclass(slots=True)
class AnalysisPipeline:

    extractor: FeatureExtractor

    pipeline: FeaturePipeline

    def extrair(
        self,
        concurso: Concurso
    ):

        return self.extractor.extrair(
            concurso
        )

    def analisar(
        self,
        concurso: Concurso
    ):

        feature = self.extrair(
            concurso
        )

        return self.pipeline.processar(
            feature
        )
    
    @classmethod
    def _default_stages(
        cls,
        analyzer: HistoricoAnalyzer,
        statistics: HistoricoStatistics,
        cadeia_somas
    ):

        return [

            *cls._probability_stages(

                analyzer,

                statistics

            ),

            *cls._statistics_stages(

                analyzer,

                statistics

            ),

            BayesStage(

                Bayes()

            ),

            MarkovStage(

                cadeia_somas,

                attrgetter("soma"),

                "markov_soma"

            ),

            ScoreStage()

        ]
    
    @classmethod
    def _features(
        cls,
        analyzer: HistoricoAnalyzer
    ) -> list[tuple[str, Callable[[], dict]]]:
                
        return [
            
            ("soma", 
            analyzer.distribuicao_somas),
            
            ("pares", 
            analyzer.distribuicao_pares),
            
            ("impares", 
            analyzer.distribuicao_impares),
            
            ("consecutivos", 
            analyzer.distribuicao_consecutivos),
            
            ("linhas", 
            analyzer.distribuicao_linhas),
            
            ("colunas", 
            analyzer.distribuicao_colunas)
            
        ]
    
    @classmethod
    def _build_stages(
        cls,
        stage_cls,
        prefixo: str,
        analyzer: HistoricoAnalyzer,
        statistics: HistoricoStatistics,
        features
    ):

        return [

            stage_cls(

                distribuicao,

                attrgetter(nome),

                f"{prefixo}_{nome}",

                statistics

            )

            for nome, distribuicao in features(

                analyzer

            )

        ]
    
    @classmethod
    def _probability_stages(
        cls,
        analyzer,
        statistics
    ):

        return cls._build_stages(

            ProbabilityStage,

            "prob",

            analyzer,

            statistics,

            cls._features

        )
    
    @classmethod
    def _numeric_features(
        cls,
        analyzer: HistoricoAnalyzer
    ):

        return [

            ("soma", analyzer.distribuicao_somas),

            ("pares", analyzer.distribuicao_pares),

            ("impares", analyzer.distribuicao_impares),

            ("consecutivos", analyzer.distribuicao_consecutivos),

        ]
    
    @classmethod
    def _statistics_stages(
        cls,
        analyzer,
        statistics
    ):

        return cls._build_stages(

            StatisticsStage,

            "zscore",

            analyzer,

            statistics,

            cls._numeric_features

        )
      
    @classmethod
    def default(
        cls,
        historico: Historico
    ):

        analyzer = HistoricoAnalyzer(

            historico

        )

        statistics = HistoricoStatistics(

            analyzer

        )

        builder = MarkovBuilder()

        cadeia_somas = builder.construir_somas(

            historico

        )

        pipeline = FeaturePipeline(

            cls._default_stages(

                analyzer,

                statistics,

                cadeia_somas

            )

        )

        return cls(

            extractor=FeatureExtractor(),

            pipeline=pipeline

        )
    
    