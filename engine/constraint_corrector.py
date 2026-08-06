from engine.number_pool import NumberPool
from engine.swap_strategy import RandomSwapStrategy, SwapContext
from modelos.lottery_set import LotterySet


class ConstraintCorrector:

    def __init__(self, strategy=None):
        self.strategy = strategy or RandomSwapStrategy()

    
    def corrigir(

        self,

        jogo,

        erros,
        
        template

    ):

        for erro in erros:

            jogo = self.corrigir_erro(

                jogo,

                erro,
                
                template

            )

        return jogo
            
    def corrigir_quantidade(

        self,

        jogo,

        conjunto_desejado,

        quantidade_esperada,
        
        template

    ):
        
        jogo = set(jogo.dezenas)
        
        atuais = [

            n

            for n in jogo

            if n in conjunto_desejado

        ]
        
        outros = [

            n

            for n in jogo

            if n not in conjunto_desejado

        ]
        
        diferenca = quantidade_esperada - len(atuais)
        
        if diferenca > 0:
            
            disponiveis = [

                n

                for n in conjunto_desejado

                if n not in jogo

            ]
            
            for _ in range(diferenca):
                
                if not disponiveis:

                    break
                
                if not outros:

                    break
                
                contexto = SwapContext(

                    jogo=list(jogo),

                    remover=outros,

                    adicionar=disponiveis,

                    template=template

                )
                
                decisao = self.strategy.escolher(contexto)

                if decisao.remover != decisao.adicionar:

                    jogo.remove(decisao.remover)

                    jogo.add(decisao.adicionar)

                outros.remove(decisao.remover)
                disponiveis.remove(decisao.adicionar)
                atuais.append(decisao.adicionar)
        
        elif diferenca < 0:
            
            sobram = abs(diferenca)
            
            disponiveis = NumberPool.complemento(

                conjunto_desejado
            )
            
            disponiveis = [

                n

                for n in disponiveis

                if n not in jogo

            ]
            
            for _ in range(sobram):
                
                contexto = SwapContext(

                    jogo=list(jogo),

                    remover=atuais,

                    adicionar=disponiveis,

                    template=template

                )

                decisao = self.strategy.escolher(contexto)

                if decisao.remover != decisao.adicionar:

                    jogo.remove(decisao.remover)

                    jogo.add(decisao.adicionar)

                atuais.remove(decisao.remover)

                disponiveis.remove(decisao.adicionar)
                
        return LotterySet(sorted(jogo))    
    
    def corrigir_erro(

        self,

        jogo,

        erro,
        
        template

    ):
        
        if not NumberPool.existe_pool(

            erro.atributo

        ):

            return jogo
        
        pool = NumberPool.obter(

            erro.atributo

        )

        return self.corrigir_quantidade(

            jogo,

            pool,

            erro.esperado,

            template

        )

 