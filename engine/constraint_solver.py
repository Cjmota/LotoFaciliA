from engine.constraint_corrector import ConstraintCorrector
from engine.game_template import GameTemplate
from modelos.lottery_set import LotterySet
from dataclasses import dataclass

from engine.constraint_error import ConstraintError



class ConstraintSolver:

    def __init__(self, strategy=None):

        self.corrector = ConstraintCorrector(strategy)
        
    
    def validar(

        self,

        jogo,

        template: GameTemplate

    ):

        dados = jogo.estatisticas_probabilidade

        erros = []

        for atributo, esperado in template.definidos().items():

            encontrado = dados[atributo]

            if encontrado != esperado:

                erros.append(

                    ConstraintError(

                        atributo=atributo,

                        esperado=esperado,

                        encontrado=encontrado,

                        diferenca=(
                            esperado - encontrado
                            if isinstance(esperado, int)
                            else None
                        )

                    )

                )
            
        return len(erros) == 0, erros
    
    def satisfaz(

        self,

        jogo,

        template

    ):
        
        ok, _ = self.validar(

            jogo,

            template

        )

        return ok
    
    def resolver(

        self,

        jogo,

        template,

        max_iteracoes=100

    ):

        if not isinstance(jogo, LotterySet):
            jogo = LotterySet(jogo)

        for _ in range(max_iteracoes):

            ok, erros = self.validar(

                jogo,

                template

            )

            if ok:

                return jogo

            jogo = self.corrector.corrigir(

                jogo,

                erros,
                
                template

            )

        raise RuntimeError(

            f"Não foi possível satisfazer "

            f"o template após "

            f"{max_iteracoes} iterações.\n"
            
            f"Template:\n{template}"

        )


