from engine.number_pool import NumberPool

class LotteryStatistics:
    
     
    ESTATISTICAS = (
            "pares",
            "impares",
            "baixas",
            "altas",
            "soma",
            "faixa_soma",
            "linhas",
            "colunas",
            "primos",
            "fibonacci",
            "centro",
            "moldura",
            "multiplos3",
            "consecutivos",
            "maior_sequencia",
            "grupos",
            "quantidade_sequencias",
            "media_sequencias",
            "isoladas",
        )
    
    ESTATISTICAS_PROBABILISTICAS = (

    "pares",
    "baixas",
    "faixa_soma",
    "consecutivos",
    "centro",
    "moldura",
    "linhas",
    "colunas",
    "primos",
    "fibonacci",
    "multiplos3",

)
    
    
    
    PRIMOS = set(

        NumberPool.primos()

    )

    FIBONACCI = set(

        NumberPool.fibonacci()

    )

    CENTRO = set(

        NumberPool.centro()

    )

    MULT3 = set(

        NumberPool.multiplos3()

    )
    

    def __init__(self, lottery):

        self.lottery = lottery
         
        self._estatisticas = None
        self._estatisticas_probabilidade = None
        
        self._sequencias_cache = self._sequencias()
    
    
    def _contar_conjunto(self, conjunto: set[int]) -> int:
        return sum(1 for n in self.dezenas if n in conjunto)
    
    def _contar(

        self,

        criterio

    ) -> int:

        return sum(criterio(n) for n in self.dezenas)
        
    
    #1º grupo
    @property
    def pares(self):

        return self._contar(

            lambda numero: numero % 2 == 0

        )

    @property
    def impares(self):

        return self.quantidade - self.pares

    @property
    def altas(self):

        return self.quantidade - self.baixas

    @property
    def baixas(self):

        return self._contar(

            lambda numero: numero <= 13

        )
 
    
    #2º Grupo
    @property
    def primos(self):

        return self._contar_conjunto(self.PRIMOS)
    
    @property
    def fibonacci(self):

        return self._contar_conjunto(self.FIBONACCI)

    @property
    def centro(self):

        return self._contar_conjunto(self.CENTRO)
    
    @property
    def moldura(self):

        return self.quantidade - self.centro
    
    @property
    def multiplos3(self):

        return self._contar_conjunto(self.MULT3)

   
    #3º Grupo
    @property
    def soma(self):
        return sum(self.dezenas)
    
    @property
    def faixa_soma(self):

        return self._faixa(
            
            self.soma,

            10

        )


    #4º Grupo
    @property
    def linhas(self):

        return self._distribuir(
            
            lambda numero: (numero - 1) // 5
        
        )

    @property
    def colunas(self):

        return self._distribuir(
            
            lambda numero: (numero - 1) % 5
        
        )
  
    
    #5º Grupo
    @property
    def sequencias(self):
        return self._sequencias_cache

    @property
    def consecutivos(self):

        return sum(

            len(grupo)-1

            for grupo in self.sequencias

        )

    @property
    def maior_sequencia(self):

        return max(

            (len(grupo) for grupo in self.sequencias),

            default=0

        )
        
    @property
    def grupos(self):

        return len(self.sequencias)

    @property
    def quantidade_sequencias(self):

        return sum(

            len(grupo) > 1

            for grupo in self.sequencias

        )

    @property
    def media_sequencias(self):

        grupos = self.sequencias

        if not grupos:

            return 0

        return sum(

            len(g)

            for g in grupos

        ) / len(grupos)
    
    @property
    def isoladas(self):

        return sum(

            len(grupo) == 1

            for grupo in self.sequencias

        )
    
   
    #6º grupo
    @property
    def estatisticas(self):
        return {
            nome: getattr(self, nome)
            for nome in self.ESTATISTICAS
        }

    @property
    def estatisticas_probabilidade(self):
        
        if self._estatisticas_probabilidade is None:

            self._estatisticas_probabilidade = {

                nome: getattr(self, nome)

                for nome in self.ESTATISTICAS_PROBABILISTICAS

            }

        return self._estatisticas_probabilidade
    
    @property
    def dezenas(self):
        return self.lottery.dezenas
    
    @property
    def quantidade(self):
        return len(self.dezenas)
   
    
    
    def _sequencias(self):

        if not self.dezenas:

            return []

        grupos = []

        grupo = [

            self.dezenas[0]

        ]

        for numero in self.dezenas[1:]:

            if numero == grupo[-1] + 1:

                grupo.append(numero)

            else:

                grupos.append(grupo)

                grupo = [numero]

        grupos.append(grupo)

        return grupos
    
    def _distribuir(

        self,

        indice

    ) -> tuple[int, int, int, int, int]:

        distribuicao = [0] * 5

        for numero in self.dezenas:

            distribuicao[indice(numero)] += 1

        return tuple(distribuicao)
    
    def _faixa(

        self,

        valor,

        tamanho

    ):

        inicio = (valor // tamanho) * tamanho

        return f"{inicio}-{inicio+tamanho-1}"

    
    