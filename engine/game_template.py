from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class GameTemplate:

    pares: Optional[int] = None

    baixas: Optional[int] = None

    centro: Optional[int] = None

    moldura: Optional[int] = None

    primos: Optional[int] = None

    fibonacci: Optional[int] = None

    multiplos3: Optional[int] = None

    consecutivos: Optional[int] = None

    faixa_soma: Optional[str] = None

    linhas: Optional[tuple] = None

    colunas: Optional[tuple] = None
    
    def to_dict(self):

        return asdict(self)
    
    def items(self):

        return self.to_dict().items()
    
    def keys(self):

        return self.to_dict().keys()
    
    def values(self):

        return self.to_dict().values()
    
    def get(self, chave, default=None):

        return self.to_dict().get(

            chave,

            default

        )
    
    def update(self, **kwargs):

        dados = self.to_dict()

        dados.update(kwargs)

        return GameTemplate(**dados)
    
    def copy(self):

        return GameTemplate(

            **self.to_dict()

        )
    
    def vazio(self):

        return all(

            valor is None

            for valor in self.values()

        )
    
    def definidos(self):

        return {

            chave: valor

            for chave, valor in self.items()

            if valor is not None

        }
    
    def quantidade_regras(self):

        return len(

            self.definidos()

        )
    
    def __iter__(self):

        return iter(self.items())
    
    def __getitem__(self, chave):

        return self.get(chave)
    
    def __len__(self):

        return len(self.to_dict())
    
    def __contains__(self, chave):

        return chave in self.to_dict()
    
    def __str__(self):

        linhas = []

        linhas.append("=" * 40)

        linhas.append("GAME TEMPLATE")

        linhas.append("=" * 40)

        for chave, valor in self:

            if valor is not None:

                linhas.append(

                    f"{chave:<15}: {valor}"

                )

        return "\n".join(linhas)
    
    def to_list(self):

        return list(

            self.values()

        )
    
    def clear(self):

        for chave in self.keys():

            setattr(

                self,

                chave,

                None

            )

        return self
    
    def merge(self, outro):

        dados = self.to_dict()

        dados.update(

            outro.definidos()

        )

        return GameTemplate(

            **dados

        )
    
    def preenchido(self):

        return not self.vazio()
    
    