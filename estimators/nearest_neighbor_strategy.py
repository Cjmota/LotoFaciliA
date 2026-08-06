from estimators.estimator_strategy import EstimatorStrategy

from modelos.weight import Weight


class NearestNeighborStrategy(EstimatorStrategy):

    def __init__(self, finder):

        super().__init__()

        self.finder = finder

    def estimar(
        self,
        repository,
        categoria,
        valor
    ):

        valores = repository.valores(categoria)

        if not valores:
            return Weight()

        mais_proximo = self.finder.nearest(
            valores,
            valor
        )

        # Informações para depuração
        self._ultimo_valor = valor
        self._ultimo_vizinho = mais_proximo
        self._ultima_distancia = abs(
            valor - mais_proximo
        )

        return repository.buscar_peso(
            categoria,
            mais_proximo
        )