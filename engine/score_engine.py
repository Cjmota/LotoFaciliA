from pathlib import Path
import json
from modelos.game_score import GameScore

BASE_DIR = Path(__file__).resolve().parent.parent

class ScoreEngine:

    def __init__(

        self,

        arquivo = BASE_DIR / "score.config.json"

    ):

        arquivo = Path(arquivo)

        if arquivo.exists():

            with open(

                arquivo,

                "r",

                encoding="utf8"

            ) as f:

                self.pesos = json.load(f)

        else:

            self.pesos = {}
               
    def peso(self, categoria):

        return self.pesos.get(

            categoria,

            1.0

        )
    
    def calcular(

        self,

        game_score: GameScore

    ) -> GameScore:

        total = 0

        soma_pesos = 0

        for categoria, feature_score in game_score:

            peso_categoria = self.peso(categoria)

            total += feature_score.score * peso_categoria

            soma_pesos += peso_categoria

        game_score.score_ponderado = total
        game_score.score_total = total

        if soma_pesos > 0:

            game_score.score_normalizado = total / soma_pesos

        else:

            game_score.score_normalizado = 0

        return game_score    