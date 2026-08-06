from dataclasses import dataclass, fields




@dataclass(frozen=True)
class Weight:

    probabilidade: float = 0.0

    peso_bayes: float = 0.0

    percentual: float = 0.0

    ranking: int = 999

    quantidade: int = 0

    nota: float = 0.0
      
    @classmethod
    def atributos_benchmark(cls):

        ignorar = {

            "ranking",

            "quantidade"

        }

        return tuple(

            campo.name

            for campo in fields(cls)

            if campo.name not in ignorar

        )
    
    @classmethod
    def from_dict(

        cls,

        dados

    ) -> "Weight":

        return cls(

            probabilidade=dados.get(

                "probabilidade",

                0.0

            ),

            peso_bayes=dados.get(

                "peso_bayes",

                0.0

            ),

            percentual=dados.get(

                "percentual",

                0.0

            ),

            ranking=dados.get(

                "ranking",

                999

            ),

            quantidade=dados.get(

                "quantidade",

                0

            ),

            nota=dados.get(

                "nota",

                0

            )

        )
        
    def to_dict(self):

        return {

            "probabilidade": self.probabilidade,

            "peso_bayes": self.peso_bayes,

            "percentual": self.percentual,

            "ranking": self.ranking,

            "quantidade": self.quantidade,

            "nota": self.nota

        }
        
    @property
    def vazio(self) -> bool:

        return self.quantidade == 0
    
    @property
    def existe(self) -> bool:

        return self.quantidade > 0
    
    def __repr__(self):

        return (

            f"Weight("

            f"ranking={self.ranking}, "

            f"prob={self.probabilidade:.4f}, "

            f"nota={self.nota:.2f}"

            f")"

        )
        
    @property
    def score_base(self) -> float:

        return (

            self.probabilidade *

            self.nota

        )
    
    @property
    def confianca(self) -> float:

        if self.ranking <= 0:

            return 0

        return self.nota / self.ranking