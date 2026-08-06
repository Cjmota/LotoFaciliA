import json

from pathlib import Path


class WeightRepository:

    def __init__(

        self,

        arquivo="pesos_estatisticos.json"

    ):

        self.arquivo = Path(arquivo)

        self._dados = None

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

            self._dados = json.load(f)
        
        return self
    
    def categoria(self):

        return tuple(

            self._dados.keys()

        )
    
    def consultar(

        self,

        categoria,

        valor

    ):

        categoria = self._dados.get(

            categoria,

            {}

        )

        return categoria.get(

            str(valor)

        )
    
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

        return dado.get(

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
    
    def __contains__(

        self,

        categoria

    ):

        return categoria in self._dados
    
    def __getitem__(

        self,

        categoria

    ):

        return self._dados[categoria]
    
    def __len__(self):

        return len(

            self._dados

        )
    
    def __iter__(self):

        return iter(

            self._dados.items()

        )
    
    def categorias(self):

        return list(

            self._dados.keys()

        )
    
    def atualizar(self):

        self.carregar()

if __name__ == "__main__":

    repo = WeightRepository()

    print()

    print(repo.categorias())

    print()

    print(

        repo.consultar(

            "Pares",

            7

        )

    )