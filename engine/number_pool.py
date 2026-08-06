import random

class NumberPool:
    
    TODOS = set(range(1, 26))

    PRIMOS = {

        2,3,5,7,

        11,13,17,19,23

    }

    FIBONACCI = {

        1,2,3,5,

        8,13,21

    }

    CENTRO = {

        7,8,9,

        12,13,14,

        17,18,19

    }
    
    @staticmethod
    def existe_pool(nome):

        return nome in NumberPool.pools()
        
    @staticmethod
    def pools():

        return {

            "pares": NumberPool.pares,

            "impares": NumberPool.impares,

            "primos": NumberPool.primos,

            "fibonacci": NumberPool.fibonacci,

            "centro": NumberPool.centro,

            "moldura": NumberPool.moldura,

            "multiplos3": NumberPool.multiplos3

        }
        
    @staticmethod
    def obter(nome):

        metodo = NumberPool.pools().get(nome)

        if metodo is None:

            nomes = ", ".join(

                NumberPool.pools().keys()

            )

            raise ValueError(

                f"Pool '{nome}' inexistente. Pools disponíveis: {nomes}"

            )

        return metodo()
    
    @staticmethod
    def todos():

        return sorted(NumberPool.TODOS)

    @staticmethod
    def pares():

        return NumberPool.filtrar(
            
            NumberPool.todos(),
            lambda n: n % 2 == 0

        )
    
    @staticmethod
    def impares():

        return NumberPool.filtrar(
            
            NumberPool.todos(),
            
            lambda n: n % 2 == 1

        )
    
    @staticmethod
    def primos():

        return sorted(

            NumberPool.PRIMOS

        )
    
    @staticmethod
    def fibonacci():

        return sorted(

            NumberPool.FIBONACCI

        )
    
    @staticmethod
    def centro():

        return sorted(NumberPool.CENTRO)
    
    @staticmethod
    def moldura():

        return sorted(NumberPool.TODOS - NumberPool.CENTRO)
    
    @staticmethod
    def multiplos3():

        return NumberPool.filtrar(
            
            NumberPool.todos(),

            lambda n: n % 3 == 0

        )

    @staticmethod
    def aleatorios(quantidade):

        return sorted(

            random.sample(

                NumberPool.todos(),

                quantidade

            )

        )
    
    @staticmethod
    def filtrar(numeros, filtro ):

        return [

            n

            for n in numeros

            if filtro(n)

        ]

    @staticmethod
    def sortear(

        numeros,

        quantidade

    ):

        return sorted(

            random.sample(

                numeros,

                quantidade

            )

        )

    @staticmethod
    def quantidade():

        return len(

            NumberPool.TODOS

        )

    @staticmethod
    def existe(numero):

        return numero in NumberPool.TODOS

    @staticmethod
    def complemento(numeros):

        return sorted(

            NumberPool.TODOS

            -

            set(numeros)

        )

    @staticmethod
    def uniao(*listas):

        resultado = set()

        for lista in listas:

            resultado.update(lista)

        return sorted(resultado)

    @staticmethod
    def intersecao(*listas):

        resultado = set(listas[0])

        for lista in listas[1:]:

            resultado &= set(lista)

        return sorted(resultado)

if __name__ == "__main__":

    print()

    print(NumberPool.pares())

    print()

    print(NumberPool.impares())

    print()

    print(NumberPool.primos())

    print()

    print(NumberPool.fibonacci())

    print()

    print(NumberPool.centro())

    print()

    print(NumberPool.moldura())

    print()

    print(NumberPool.multiplos3())