from benchmarks.benchmark_metrics import BenchmarkMetrics

from benchmarks.benchmark_report import BenchmarkReport

from statistics import median

from statistics import pstdev

from math import fabs, sqrt

from modelos.weight import Weight


class BenchmarkStatistics:

    def __init__(self, resultados):

        self.resultados = resultados

    def resumo(self, atributo):

        if not self._preparar(atributo):
            return BenchmarkMetrics(

                atributo=atributo,

                quantidade=0,

                mae=0.0,

                rmse=0.0,

                erro_maximo=0.0,

                erro_minimo=0.0,

                mediana=0.0,

                desvio_padrao=0.0

            )
        
        erros = self._erros(atributo)

        return BenchmarkMetrics(

            atributo=atributo,

            quantidade=len(erros),

            mae=self._mae(erros),

            rmse=self._rmse(erros),

            erro_maximo=self._maximo(erros),

            erro_minimo=self._minimo(erros),

            mediana=self._mediana(erros),

            desvio_padrao=self._desvio_padrao(erros)

        )    
        
        
    def mae(self, atributo):

        if not self._preparar(atributo):
            return 0.0

        erros = self._erros(atributo)

        return self._mae(erros)
    
    def rmse(self, atributo):

        if not self._preparar(atributo):
            return 0.0

        erros = self._erros(atributo)

        return self._rmse(erros)
    
    def erro_maximo(self, atributo):
    
        if not self._preparar(atributo):
            return 0.0
    
        erros = self._erros(atributo)

        return self._maximo(erros)
    
    def erro_minimo(self, atributo):

        if not self._preparar(atributo):
            return 0.0

        erros = self._erros(atributo)
        
        return self._minimo(erros)
    
    def mediana(self, atributo):

        if not self._preparar(atributo):
            return 0.0

        erros = self._erros(atributo)

        return self._mediana(erros)
    
    def desvio_padrao(self, atributo):

        if not self._preparar(atributo):
            return 0.0

        erros = self._erros(atributo)

        return self._desvio_padrao(erros)
    
    
    def resumo_completo(self):

        if not self.resultados:
            return BenchmarkReport({})

        return BenchmarkReport({

            atributo: self.resumo(atributo)

            for atributo

            in Weight.atributos_benchmark()

        })
        
    def _preparar(self, atributo):

        if not self.resultados:
            return False

        self._validar_atributo(atributo)

        return True
        
    
    def _erros(self, atributo):

        return [

            fabs(real - estimado)

            for real, estimado

            in self._iterar_pares(atributo)

        ]
    
    
    def _iterar_pares(self, atributo):

        for resultado in self.resultados:

            yield (

                getattr(resultado.real, atributo),

                getattr(resultado.estimado, atributo)

            )
    
    
    def _mae(self, erros):

        return sum(erros) / len(erros)
        
    def _rmse(self, erros):

        return sqrt(

            sum(

                e ** 2

                for e in erros

            )

            / len(erros)

        )
        
    def _maximo(self, erros):

        return max(erros)
    
    def _minimo(self, erros):
    
        return min(erros)
    
    def _mediana(self, erros):
        
        return median(erros)
    
    def _desvio_padrao(self, erros):
            
        return pstdev(erros)
    
        
    def _validar_atributo(self, atributo):

        if not self.resultados:
            return

        if not hasattr(self.resultados[0].real, atributo):
            raise ValueError(
                f"Atributo '{atributo}' não existe em Weight."
            )
    
  