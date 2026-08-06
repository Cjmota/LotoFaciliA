from estimators.estimator_strategy import EstimatorStrategy

from modelos.weight import Weight


class InterpolationStrategy(EstimatorStrategy):

    def __init__(
        self,
        finder,
        interpolator
    ):

        super().__init__()

        self.finder = finder
        self.interpolator = interpolator

    def estimar(
        self,
        repository,
        categoria,
        valor
    ):

        valores = repository.valores(categoria)

        if not valores:
            return Weight()
        
        # Existe exatamente esse valor?
        if repository.existe(categoria, valor):
            return repository.buscar_peso(
                categoria,
                valor
            )

        inferior = self.finder.lower(
            valores,
            valor
        )

        superior = self.finder.upper(
            valores,
            valor
        )
        
        # Guarda informações para depuração
        self._ultimo_valor = valor
        self._ultimo_inferior = inferior
        self._ultimo_superior = superior
        

        if inferior is None and superior is None:
            return Weight()

        if inferior is None:
            return repository.buscar_peso(
                categoria,
                superior
            )

        if superior is None:
            return repository.buscar_peso(
                categoria,
                inferior
            )

        peso_inferior = repository.buscar_peso(
            categoria,
            inferior
        )

        peso_superior = repository.buscar_peso(
            categoria,
            superior
        )

        return self.interpolator.interpolar(
            valor_inferior=inferior,
            peso_inferior=peso_inferior,
            valor_superior=superior,
            peso_superior=peso_superior,
            valor_procurado=valor
        )