from pathlib import Path

from modelos.concurso import Concurso

from modelos.historico import Historico

import pandas as pd

class HistoryRepository:

    COLUNAS_BOLAS = tuple(

        f"Bola{i}"

        for i in range(1,16)

    )

    def __init__(

        self,

        arquivo="dados/Lotofacil.xlsx"

    ):

        BASE_DIR = Path(__file__).resolve().parent.parent

        self.arquivo = BASE_DIR / arquivo

        self.df = None
        
        self._historico = None

        self.carregar()
        
    def carregar(self):

        if not self.arquivo.exists():

            raise FileNotFoundError(

                self.arquivo

            )

        self.df = pd.read_excel(

            self.arquivo

        )

        return self
    
    def jogo_por_indice(

        self,

        indice

    ):

        linha = self.df.iloc[indice]

        return [

            int(linha[coluna])

            for coluna in self.COLUNAS_BOLAS

        ]

    def jogo_por_concurso(

        self,

        numero

    ):

        return self.concurso(

            numero

        ).dezenas

    def concurso(

        self,

        numero

    ):

        linha = self.df.loc[

            self.df["Concurso"] == numero

        ]

        if linha.empty:

            raise ValueError(

                f"Concurso {numero} inexistente."

            )

        linha = linha.iloc[0]

        return self._criar_concurso(linha)
       
    def numeros_concursos(self):

        return self.df["Concurso"].tolist()
    
    def datas(self):

        return self.df["Data Sorteio"].tolist()
           
    def todos_os_jogos(self):

        return [

            self.jogo_por_indice(i)

            for i in range(

                self.quantidade()

            )

        ]   
              
    def ultimo_jogo(self):

        return self.concurso(

            self.numeros_concursos()[-1]

        )
        
    def quantidade(self):

        return len(

            self.df

        )    
    
    def historico(self):

        if self._historico is not None:

            return self._historico

        historico = Historico()

        for _, linha in self.df.iterrows():

            historico.adicionar(

                self._criar_concurso(linha)

            )

        self._historico = historico

        return self._historico
    
    def _criar_concurso(

        self,

        linha

    ):

        return Concurso(

            numero=int(linha["Concurso"]),

            data=pd.to_datetime(

                linha["Data Sorteio"],

                format="%d/%m/%Y"

            ),

            dezenas=[

                int(linha[coluna])

                for coluna in self.COLUNAS_BOLAS

            ],

            ganhadores_15=int(

                linha["Ganhadores 15 acertos"]

            ),

            cidade_uf=str(

                linha["Cidade / UF"]

            ),

            rateio_15=str(

                linha["Rateio 15 acertos"]

            )

        )
    
if __name__ == "__main__":

    repo = HistoryRepository()

    print()

    print("Total:")

    print(repo.quantidade())

    print()

    print("Primeiro:")

    print(repo.jogo_por_indice(0))

    print()

    print("Último:")

    print(repo.ultimo_jogo())

    print()

    print("Concurso 100:")

    print(repo.jogo_por_concurso(100))