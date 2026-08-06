from dataclasses import dataclass, field

from modelos.game_score import GameScore

from modelos.lottery_set import LotterySet
  
    
@dataclass
class Game(LotterySet):

    score: GameScore | None = None

    valido: bool = False

    erros: list[str] = field(default_factory=list)
    
    
    def valido_sem_erros(self) -> bool:

        return self.valido and not self.erros
    
    def adicionar_erro(

        self,

        erro

    ):

        self.erros.append(erro)
    
    def limpar_erros(self):

        self.erros.clear()
    

    def definir_score(

        self,

        score: GameScore

    ):

        self.score = score

        return self

    def atualizar_validacao(

        self,

        valido: bool,

        erros: list[str]

    ):

        self.valido = valido

        self.erros = list(erros)

        return self
 
    def copy(self):

        from copy import deepcopy

        return deepcopy(self)
   
    def __str__(self):

        return (

            f"Game("

            f"dezenas={self.dezenas}, "

            f"valido={self.valido}, "

            f"score={self.score.score_total if self.score else 0:.2f}"

            f")"

        )
    
    def __repr__(self):

        return self.__str__()
    
    @property
    def tem_score(self) -> bool:

        return self.score is not None
    
   
   
    @property
    def invalido(self):

        return not self.valido
    
    @property
    def quantidade_erros(self):

        return len(self.erros)

    @property
    def pronta(self):

        return self.tem_score
    
    @property
    def game_score(self):

        return self.score or GameScore()
    
    @property
    def score_total(self):

        if self.score is None:

            return 0

        return self.score.score_total
    
    @property
    def score_normalizado(self):
        
        if self.score is None:

            return 0

        return self.game_score.score_normalizado
    
    @property
    def score_ponderado(self):
        
        if self.score is None:

            return 0

        return self.game_score.score_ponderado
