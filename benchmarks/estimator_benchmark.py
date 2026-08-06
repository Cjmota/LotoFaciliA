from estimators.weight_estimator import WeightEstimator

from dataclasses import dataclass

from benchmarks.benchmark_result import BenchmarkResult


class EstimatorBenchmark:

    def __init__(self, repository):

        self.repository = repository

        self.resultados = []

    def limpar(self):

        self.resultados.clear()

    def avaliar(

        self,

        estimator,

        categoria

    ):

        self.limpar()

        valores = self.repository.valores(
            categoria
        )

        for valor in valores:

            repo_teste = self.repository.sem_valor(
                categoria,
                valor
            )

            estimator_teste = WeightEstimator(

                repo_teste,

                strategy=estimator.strategy

            )

            peso_real = self.repository.buscar_peso(

                categoria,

                valor

            )

            peso_estimado = estimator_teste.resolver(

                categoria,

                valor

            )

            self.resultados.append(

                BenchmarkResult(

                    categoria=categoria,

                    valor=valor,

                    real=peso_real,

                    estimado=peso_estimado

                )

            )

        return self.resultados