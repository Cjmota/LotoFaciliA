from dataclasses import dataclass

from modelos.statistics.lottery_statistics import LotteryStatistics


@dataclass
class LotterySet:
   
    dezenas: list[int]
    
    
    def __post_init__(self):

        self.dezenas = sorted(map(int, self.dezenas))
        
        self._statistics = LotteryStatistics(self)
        
        
    @property
    def estatisticas(self):
        return self._statistics.estatisticas
    
    @property
    def estatisticas_probabilidade(self):
        return self._statistics.estatisticas_probabilidade
    
    @property
    def chave(self):
        return tuple(self.dezenas)
    
    @property
    def quantidade(self):
        return len(self.dezenas)
    
    @property
    def primeiro(self):
        return self.dezenas[0] if self.dezenas else None
    
    @property
    def ultimo(self):
        return self.dezenas[-1] if self.dezenas else None
    
    @property
    def pares(self):
        return self._statistics.pares

    @property
    def impares(self):
        return self._statistics.impares

    @property
    def baixas(self):
        return self._statistics.baixas
    
    @property
    def altas(self):
        return self._statistics.altas

    @property
    def primos(self):
        return self._statistics.primos

    @property
    def fibonacci(self):
        return self._statistics.fibonacci

    @property
    def centro(self):
        return self._statistics.centro

    @property
    def moldura(self):
        return self._statistics.moldura

    @property
    def multiplos3(self):
        return self._statistics.multiplos3

    @property
    def soma(self):
        return self._statistics.soma

    @property
    def faixa_soma(self):
        return self._statistics.faixa_soma

    @property
    def linhas(self):
        return self._statistics.linhas

    @property
    def colunas(self):
        return self._statistics.colunas

    @property
    def sequencias(self):
        return self._statistics.sequencias

    @property
    def consecutivos(self):
        return self._statistics.consecutivos

    @property
    def maior_sequencia(self):
        return self._statistics.maior_sequencia

    @property
    def grupos(self):
        return self._statistics.grupos

    @property
    def quantidade_sequencias(self):
        return self._statistics.quantidade_sequencias

    @property
    def media_sequencias(self):
        return self._statistics.media_sequencias

    @property
    def isoladas(self):
        return self._statistics.isoladas
    
    
    def contem(

        self,

        numero

    ):

        return numero in self.dezenas

    def intersecao(

        self,

        outro

    ):

        return sorted(

            set(self.dezenas)

            &

            set(outro.dezenas)

        )
    
    def diferenca(

        self,

        outro

    ):

        return sorted(

            set(self.dezenas)

            ^

            set(outro.dezenas)

        )
    
    def acertos(

        self,

        outro

    ):

        return len(

            self.intersecao(outro)

        )
    
    def similaridade(

        self,

        outro

    ):

        return (

            self.acertos(outro)

            /

            self.quantidade

        )
    
    def distancia(

        self,

        outro

    ):

        return (

            self.quantidade

            -

            self.acertos(outro)

        )
    
    
    
    def __iter__(self):

        return iter(self.dezenas)

    def __len__(self):

        return len(self.dezenas)

    def __eq__(

        self,

        outro

    ):

        if not isinstance(outro, LotterySet):

            return False

        return self.chave == outro.chave
    
    def __hash__(self):

        return hash(self.chave)

    def __repr__(self):

        return (

            f"{self.__class__.__name__}"

            f"({self.dezenas})"

        )
    