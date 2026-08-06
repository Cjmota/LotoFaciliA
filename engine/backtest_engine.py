from engine.feature_engine import extrair_features
from engine.validator_engine import ValidatorEngine
from engine.probability_engine import ProbabilityEngine
from engine.score_engine import ScoreEngine
from dataclasses import dataclass
from dataclasses import field

import pandas as pd

@dataclass

class BacktestResult:

    total: int = 0

    aprovados: int = 0

    rejeitados: int = 0

    score_medio: float = 0

    melhor_score: float = 0

    pior_score: float = 999
    
    jogos: list = field(default_factory=list)
    
    @property
    def percentual(self):

        if self.total == 0:

            return 0

        return self.aprovados / self.total * 100
    
    def __str__(self):

        linhas = []

        linhas.append("=" * 50)
        linhas.append("BACKTEST RESULT")
        linhas.append("=" * 50)
        linhas.append(f"Total.............: {self.total}")
        linhas.append(f"Aprovados........: {self.aprovados}")
        linhas.append(f"Rejeitados.......: {self.rejeitados}")
        linhas.append(f"Percentual.......: {self.percentual:.2f}%")
        linhas.append(f"Score Médio......: {self.score_medio:.3f}")
        linhas.append(f"Melhor Score.....: {self.melhor_score:.3f}")
        linhas.append(f"Pior Score.......: {self.pior_score:.3f}")

        return "\n".join(linhas)
    
    def __len__(self):

        return len(self.jogos)

    def __iter__(self):

        return iter(self.jogos)

    def __getitem__(self, index):

        return self.jogos[index]
    
class BacktestEngine:

    def __init__(

        self,

        arquivo="lotofacil.xlsx"

    ):

        self.df = pd.read_excel(arquivo)

        self.validator = ValidatorEngine()

        self.probability = ProbabilityEngine()

        self.score = ScoreEngine()
    
    def executar(self):

        resultado = BacktestResult()

        soma_scores = 0
        
        for _, linha in self.df.iterrows():

            bolas = sorted(

                int(linha[f"Bola{i}"])

                for i in range(1,16)

            )

            resultado.total += 1
        
            game = self.game.avaliar(bolas)

            resultado.jogos.append(game)

            if game.valido:

                resultado.aprovados += 1

            else:

                resultado.rejeitados += 1
            
            contador = {}

            for jogo in resultado:

                for erro in jogo.erros:

                    contador[erro] = contador.get(erro,0)+1
            
            resultado.jogos.append(game)
            
            resultado.aprovados += 1

            soma_scores += game.score_total           
            
            if game.score_total > resultado.melhor_score:

                resultado.melhor_score = game.score_total
            
            if game.score_total < resultado.pior_score:

                resultado.pior_score = game.score_total
        
        if resultado.aprovados:

            resultado.score_medio = (

                soma_scores /

                resultado.aprovados

            )
            
            resultado.rejeitados = (

                resultado.total -

                resultado.aprovados

            )
            
            return resultado

if __name__ == "__main__":

    backtest = BacktestEngine()

    resultado = backtest.executar()

    print(resultado)
