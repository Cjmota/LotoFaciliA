from dataclasses import dataclass, field

from typing import List

from modelos.feature_score import FeatureScore

from collections import OrderedDict

from modelos.lottery_set import LotterySet

@dataclass
class GameScore:
    """
    Representa toda a avaliação
    estatística de um jogo.
    """

    jogo: LotterySet | None = None    

    scores: OrderedDict[str, FeatureScore] = field(default_factory=OrderedDict)

    score_total: float = 0.0

    score_normalizado: float = 0.0
    
    score_ponderado: float = 0.0

    probabilidade: float = 0.0
    
    media: float = 0.0

    observacao: str = ""
    
    valido: bool = True
    
    erros: List[str] = field(default_factory=list)
    
    def adicionar(self, score: FeatureScore):

        self.scores[score.nome] = score
        
        self._recalcular()
       
    def _recalcular(self):

        if not self.scores:

            self.score_total = 0.0
            self.score_normalizado = 0.0
            self.score_ponderado = 0.0
            self.probabilidade = 0.0
            self.media = 0.0

            return

        quantidade = len(self.scores)

        self.score_total = sum(
            s.score
            for s in self.scores.values()
        )

        self.probabilidade = (
            sum(
                s.probabilidade
                for s in self.scores.values()
            )
            / quantidade
        )

        self.media = self.score_total / quantidade

        self.score_normalizado = self.media
       
    def __getitem__(self, nome):

        return self.scores[nome]

    def items(self):

        return self.scores.items()

    def values(self):

        return self.scores.values()

    def keys(self):

        return self.scores.keys()

    def get(self, chave, default=None):

        return self.scores.get(chave, default)

    def to_dict(self):

        return {


            "score_total": self.score_total,

            "score_normalizado": self.score_normalizado,

            "probabilidade": self.probabilidade,

            "observacao": self.observacao,
            
            "valido": self.valido,

            "erros": self.erros,

            "scores": {

                nome: item.to_dict()

                for nome, item in self.scores.items()

            }

        } 
  
    def __iter__(self):

        return iter(self.scores.items())
   
    def __len__(self):

        return len(self.scores)

    def __contains__(self, nome):

        return nome in self.scores

    def __str__(self):

        linhas = []

        linhas.append("=" * 50)

        linhas.append("GAME SCORE")

        linhas.append("=" * 50)

        linhas.append("")

        for item in self.scores.values():

            linhas.append(str(item))

        linhas.append("")

        linhas.append(
            f"Score Total: {self.score_total:.3f}"
        )

        linhas.append(
            f"Probabilidade: {self.probabilidade:.4f}"
        )

        return "\n".join(linhas)
  
    def validar(

        self,

        valido: bool,

        erros=None

    ):

        self.valido = valido

        self.erros = erros or []

        return self
  
    
    @property
    def melhor(self):

        if not self.scores:

            return None

        return max(

            self.scores.values(),

            key=lambda s: s.score

        )
    
    @property
    def pior(self):
        
        if not self.scores:

            return None

        return min(

            self.scores.values(),

            key=lambda s: s.score

        )
              
    @property
    def aprovado(self):

        return self.valido
  
    @property
    def rejeitado(self):

        return not self.valido
  
    @property
    def quantidade(self):

        return len(self.scores)
  
    @property
    def soma_notas(self):

        return sum(

            score.nota

            for score in self.scores.values()

        )
  
    @property
    def nota_media(self):

        if not self.scores:

            return 0

        return (

            self.soma_notas

            / self.quantidade

        )
  
    @property
    def ranking_medio(self):

        if not self.scores:

            return 999

        return (

            sum(

                s.ranking

                for s in self.scores.values()

            )

            / self.quantidade

        )
    
    @property
    def melhor_nome(self):

        if self.melhor is None:

            return ""

        return self.melhor.nome
    
    @property
    def pior_nome(self):

        if self.pior is None:

            return ""

        return self.pior.nome
