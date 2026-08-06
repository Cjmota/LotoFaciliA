import json

from pathlib import Path

from modelos.weight import Weight


class ProbabilityRepository:

    def __init__(

        self,

        arquivo="pesos_estatisticos.json"

    ):

        self.arquivo = Path(arquivo)

        self._dados = {}

        self.carregar()
    
    def carregar(self):

        if not self.arquivo.exists():

            raise FileNotFoundError(

                self.arquivo

            )

        with open(

            self.arquivo,

            "r",

            encoding="utf8"

        ) as f:

            self._dados = {
            chave.lower(): valor
            for chave, valor in json.load(f).items()
        }

        return self
    
    def categorias(self):

        return tuple(

            self._dados.keys()

        )
    
    def consultar(
        self,
        categoria,
        valor
    ) -> Weight | None:

        categoria = categoria.lower()

        dados_categoria = self._dados.get(categoria)

        if dados_categoria is None:
            return None

        dados = dados_categoria.get(str(valor))

        if dados is None:
            return None

        return Weight.from_dict(dados)
        
        
    def obter(

        self,

        categoria,

        valor,

        campo,

        default=None

    ):

        dado = self.consultar(

            categoria,

            valor

        )

        if dado is None:

            return default

        return getattr(

            dado,

            campo,

            default

        )
    
    def existe(

        self,

        categoria,

        valor

    ):

        return (

            self.consultar(

                categoria,

                valor

            )

            is not None

        )
    
    def __getitem__(

        self,

        categoria

    ):

        return self._dados[categoria]
    
    def __contains__(

        self,

        categoria

    ):

        return categoria in self._dados
    
    def __len__(self):

        return len(

            self._dados

        )
    
    def __iter__(self):

        return iter(

            self._dados.items()

        )
    
    