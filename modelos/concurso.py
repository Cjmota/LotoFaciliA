from dataclasses import dataclass
from datetime import datetime
from engine.number_pool import NumberPool
from modelos.lottery_set import LotterySet


@dataclass
class Concurso(LotterySet):

    numero: int

    data: datetime

    ganhadores_15: int = 0

    cidade_uf: str = ""

    rateio_15: str = ""

    
    @property
    def id(self):

        return self.numero

    @property
    def estatisticas(self):

        dados = super().estatisticas

        dados.update({

            "consecutivos": self.consecutivos,

            "maior_sequencia": self.maior_sequencia,

            "grupos": self.grupos,

            "isoladas": self.isoladas,

            "media_sequencias": self.media_sequencias

        })

        return dados
  
    