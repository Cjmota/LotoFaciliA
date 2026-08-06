from dataclasses import dataclass

from typing import Any

from engine.game_template import GameTemplate

@dataclass
class TemplateRule:

    atributo: str

    valor: Any

class TemplateEngine:

    def __init__(self):

        pass
    
    def regras(

        self,

        template: GameTemplate

    ):
        
        regras = []
        
        for atributo, valor in template:

            if valor is None:

                continue

            regras.append(

                TemplateRule(

                    atributo,

                    valor

                )

            )
            
        return regras