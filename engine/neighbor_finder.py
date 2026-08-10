
class NeighborFinder:

    def closest(
        self,
        valores,
        procurado
    ):
        return self.nearest(
            valores,
            procurado
        )

    def nearest(
        self,
        valores,
        procurado
    ):

        if not valores:
            return None

        # Categorias vetoriais:
        # Linhas e Colunas.
        if (
            isinstance(procurado, tuple)
            and isinstance(valores[0], tuple)
        ):

            return min(
                valores,
                key=lambda valor: sum(
                    abs(a - b)
                    for a, b in zip(
                        valor,
                        procurado
                    )
                )
            )

        # Categorias numéricas:
        # Pares, Fibonacci, Consecutivos etc.
        return min(
            valores,
            key=lambda valor: abs(
                valor - procurado
            )
        )

    def lower(
        self,
        valores,
        procurado
    ):

        candidatos = [

            valor

            for valor in valores

            if valor < procurado

        ]

        if not candidatos:
            return None

        return candidatos[-1]

    def upper(
        self,
        valores,
        procurado
    ):

        candidatos = [

            valor

            for valor in valores

            if valor > procurado

        ]

        if not candidatos:
            return None

        return candidatos[0]

    def neighbors(
        self,
        valores,
        procurado
    ):

        return (

            self.lower(
                valores,
                procurado
            ),

            self.upper(
                valores,
                procurado
            )

        )