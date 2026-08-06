class BaseStatistics:

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from modelos.lottery_set import LotterySet


    def __init__(self, lottery: "LotterySet"):
        
        self.lottery = lottery        
        self._sequencias_cache = self._sequencias()

    @property
    def dezenas(self):
        return self.lottery.dezenas

    @property
    def quantidade(self):
        return len(self.dezenas)


    def _contar(

        self,

        criterio

    ) -> int:

        return sum(criterio(n) for n in self.dezenas)

    def _contar_conjunto(self, conjunto: set[int]) -> int:
        return sum(1 for n in self.dezenas if n in conjunto)

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

    