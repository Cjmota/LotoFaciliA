from dataclasses import dataclass, field

from modelos.concurso import Concurso


@dataclass
class Historico:

    concursos: list[Concurso] = field(default_factory=list)

    def adicionar(

        self,

        concurso: Concurso

    ):

        self.concursos.append(

            concurso

        )

        return self

    def quantidade(self):

        return len(

            self.concursos

        )
    
    def primeiro(self):

        return self.concursos[0]

    def ultimo(self):

        return self.concursos[-1]

    def todos(self):

        return self.concursos

    def por_numero(

        self,

        numero

    ):

        for concurso in self.concursos:

            if concurso.numero == numero:

                return concurso

        return None

    def ultimos(

        self,

        quantidade

    ):

        return self.concursos[-quantidade:]

    def intervalo(

        self,

        inicio,

        fim

    ):

        return [

            c

            for c in self.concursos

            if inicio <= c.numero <= fim

        ]

    def __iter__(self):

        return iter(

            self.concursos

        )

    def __len__(self):

        return len(

            self.concursos

        )

    def __getitem__(

        self,

        item

    ):

        return self.concursos[item]

    def __contains__(

        self,

        numero

    ):

        return self.por_numero(

            numero

        ) is not None
        
    
    