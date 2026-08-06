from dataclasses import dataclass

from domain.concurso import Concurso


@dataclass(slots=True)
class Historico:

    concursos: list[Concurso]

    def primeiro(self) -> Concurso:

        return self.concursos[0]
    
    def ultimo(self) -> Concurso:

        return self.concursos[-1]
    
    def obter(
        self,
        numero: int
    ) -> Concurso:

        for concurso in self.concursos:

            if concurso.numero == numero:

                return concurso

        raise KeyError(
            f"Concurso '{numero}' não encontrado."
        )
        
    def __contains__(
        self,
        numero: int
    ) -> bool:

        return any(

            concurso.numero == numero

            for concurso in self.concursos

        )
        
    def __len__(self):
    
            return len(self.concursos)
    
    def __iter__(self):

        return iter(self.concursos)
    
    