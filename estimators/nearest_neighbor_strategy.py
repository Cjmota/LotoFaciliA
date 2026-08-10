from estimators.estimator_strategy import EstimatorStrategy

from modelos.weight import Weight


class NearestNeighborStrategy(EstimatorStrategy):

    def __init__(self, finder):

        super().__init__()

        self.finder = finder

    def _valor_numerico(self, valor):

        if isinstance(valor, (int, float)):

            return float(valor)

        if isinstance(valor, str):

            if "-" in valor:

                partes = valor.split("-")

                if len(partes) == 2:

                    inicio = float(partes[0])
                    fim = float(partes[1])

                    return (inicio + fim) / 2

        return None

    def _distancia_tupla(self, a, b):

        return sum(
            abs(x - y)
            for x, y in zip(a, b)
        )

    def estimar(
        self,
        repository,
        categoria,
        valor
    ):

        valores = repository.valores(categoria)

        if not valores:

            return Weight()

        # ==========================================
        # CATEGORIAS TEXTUAIS / FAIXAS
        # ==========================================

        if isinstance(valor, str):

            # Correspondência exata.
            if valor in valores:

                self._ultimo_valor = valor
                self._ultimo_vizinho = valor
                self._ultima_distancia = 0

                return repository.buscar_peso(
                    categoria,
                    valor
                )

            # Caso seja uma faixa numérica,
            # como "120-129".
            valor_numerico = self._valor_numerico(
                valor
            )

            if valor_numerico is None:

                return Weight()

            candidatos = []

            for item in valores:

                item_numerico = self._valor_numerico(
                    item
                )

                if item_numerico is None:

                    continue

                distancia = abs(
                    valor_numerico -
                    item_numerico
                )

                candidatos.append(
                    (
                        distancia,
                        item
                    )
                )

            if not candidatos:

                return Weight()

            distancia, mais_proximo = min(
                candidatos,
                key=lambda item: item[0]
            )

            self._ultimo_valor = valor
            self._ultimo_vizinho = mais_proximo
            self._ultima_distancia = distancia

            return repository.buscar_peso(
                categoria,
                mais_proximo
            )

        # ==========================================
        # CATEGORIAS VETORIAIS
        # ==========================================

        if isinstance(valor, tuple):

            if not valores:

                return Weight()

            if not isinstance(valores[0], tuple):

                return Weight()

            mais_proximo = min(
                valores,
                key=lambda item: self._distancia_tupla(
                    item,
                    valor
                )
            )

            distancia = self._distancia_tupla(
                valor,
                mais_proximo
            )

            self._ultimo_valor = valor
            self._ultimo_vizinho = mais_proximo
            self._ultima_distancia = distancia

            return repository.buscar_peso(
                categoria,
                mais_proximo
            )

        # ==========================================
        # CATEGORIAS NUMÉRICAS
        # ==========================================

        mais_proximo = self.finder.nearest(
            valores,
            valor
        )

        if mais_proximo is None:

            return Weight()

        self._ultimo_valor = valor
        self._ultimo_vizinho = mais_proximo
        self._ultima_distancia = abs(
            valor - mais_proximo
        )

        return repository.buscar_peso(
            categoria,
            mais_proximo
        )