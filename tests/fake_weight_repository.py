from modelos.weight import Weight

from copy import deepcopy


class FakeWeightRepository:

    def __init__(self):

        self._dados = {
            "Pares": {
                10: Weight(
                    probabilidade=10,
                    peso_bayes=20,
                    percentual=30,
                    ranking=1,
                    quantidade=100,
                    nota=80
                ),
                20: Weight(
                    probabilidade=20,
                    peso_bayes=40,
                    percentual=50,
                    ranking=3,
                    quantidade=200,
                    nota=100
                ),
            }
        }

    def existe(
        self,
        categoria,
        valor
    ):

        return valor in self._dados.get(
            categoria,
            {}
        )

    def valores(self, categoria):

        return tuple(sorted(self._dados[categoria].keys()))

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
                valor,
                None
            )

        novo = FakeWeightRepository()

        novo._dados = dados

        return novo

    def buscar_peso(self, categoria, valor):

        return self._dados[categoria].get(
            valor,
            Weight()
        )