from abc import ABC, abstractmethod
from modelos.lottery_set import LotterySet
import random
from dataclasses import dataclass
from typing import List

@dataclass
class SwapDecision:

    remover: int

    adicionar: int

    custo: float

@dataclass
class SwapContext:

    jogo: List[int]

    remover: List[int]

    adicionar: List[int]

    template: object
    
    lottery: LotterySet | None = None

class SwapStrategy(ABC):

    @abstractmethod
    def escolher(

        self,

        contexto: SwapContext

    ):
        pass

class BaseSwapStrategy(SwapStrategy):

    def trocar(

        self,

        jogo: List[int],

        remover: int,

        adicionar: int

    ) -> List[int]:

        novo = list(jogo)

        if remover not in novo:

            return novo

        if adicionar in novo:

            return novo

        novo.remove(remover)

        novo.append(adicionar)

        novo.sort()

        return novo

    def custo(

        self,

        jogo,

        template

    ):

        lottery = LotterySet(jogo)

        dados = lottery.estatisticas

        erro = 0

        for atributo, esperado in template.definidos().items():

            encontrado = dados.get(atributo)

            if isinstance(esperado, int):

                erro += abs(

                    esperado -

                    encontrado

                )

        return erro

    def avaliar(

        self,

        jogo: List[int],

        template

    ) -> float:

        return self.custo(

            jogo,

            template

        )

class RandomSwapStrategy(BaseSwapStrategy):

    def escolher(

        self,

        contexto: SwapContext

    ):

        return SwapDecision(

            remover=random.choice(contexto.remover),

            adicionar=random.choice(contexto.adicionar),

            custo=999

        )
        
class MinimumImpactSwapStrategy(BaseSwapStrategy):

    def escolher(

        self,

        contexto: SwapContext

    ):
        melhor_remover = None

        melhor_adicionar = None

        menor_custo = float("inf")
        
        for velho in contexto.remover:

            for novo in contexto.adicionar:
                
                novo_jogo = self.trocar(

                    contexto.jogo,

                    velho,

                    novo

                )
                
                custo = self.avaliar(

                    novo_jogo,

                    contexto.template

                )
                
                if custo < menor_custo:

                    menor_custo = custo

                    melhor_remover = velho

                    melhor_adicionar = novo
                
        return SwapDecision(

            remover=melhor_remover,

            adicionar=melhor_adicionar,

            custo=menor_custo

        )
   
   
if __name__ == "__main__":

    contexto = SwapContext(

        jogo=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],

        remover=[1,3,5],

        adicionar=[20,22,24],

        template=None

    )

    estrategia = MinimumImpactSwapStrategy()

    estrategia.escolher(contexto)