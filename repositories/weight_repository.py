import json

from copy import deepcopy

from pathlib import Path

from modelos.weight import Weight


class WeightRepository:

    def __init__(

        self,

        arquivo="pesos_estatisticos.json",

        dados=None

    ):

        self.arquivo = Path(arquivo)

        if dados is None:

            self._dados = None

            self.carregar()

        else:

            self._dados = dados
    
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
    
    def categorias(self):

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
    
    def buscar_peso(

        self,

        categoria: str,

        valor

    ) -> Weight:

        dado = self.consultar(

            categoria,

            valor

        )

        if dado is None:

            return Weight()

        return Weight.from_dict(dado)
    
    def valores(self, categoria):

        return tuple(

            sorted(

                map(

                    int,

                    self._dados

                        .get(categoria, {})

                        .keys()

                )

            )

        )
    
    def sem_valor(

        self,

        categoria,

        valor

    ):

        dados = deepcopy(

            self._dados

        )

        categoria_dados = dados.get(

            categoria

        )

        if categoria_dados is not None:

            categoria_dados.pop(

                str(valor),

                None

            )

        return WeightRepository(

            arquivo=self.arquivo,

            dados=dados

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