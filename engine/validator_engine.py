import json

from pathlib import Path

from dataclasses import dataclass

from modelos.lottery_set import LotterySet

from typing import TYPE_CHECKING


@dataclass
class Rule:

    nome: str
    atributo: str
    minimo: int
    maximo: int
    mensagem: str

    
    if TYPE_CHECKING:
        from modelos.lottery_set import LotterySet


    def validar(self, jogo: "LotterySet"):

        valor = getattr(

            jogo,

            self.atributo

        )

        return self.minimo <= valor <= self.maximo
    
REGRAS_PADRAO = [

    Rule(
        nome="Pares",
        atributo="pares",
        minimo=5,
        maximo=9,
        mensagem="Quantidade de pares fora do padrão"
    ),

    Rule(
        nome="Baixas",
        atributo="baixas",
        minimo=6,
        maximo=10,
        mensagem="Baixas fora do padrão"
    ),

    Rule(
        nome="Centro",
        atributo="centro",
        minimo=3,
        maximo=7,
        mensagem="Centro improvável"
    ),

    Rule(
        nome="Consecutivos",
        atributo="consecutivos",
        minimo=5,
        maximo=10,
        mensagem="Consecutivos improváveis"
    )

]

class ValidatorEngine:

    def __init__(

        self,

        arquivo="validator_rules.json"

    ):

        self.regras = []

        self.carregar_regras(arquivo)

    def adicionar_regra(self, regra):

        self.regras.append(regra)

    def validar(self, jogo):

        erros = []

        for regra in self.regras:

            if not regra.validar(jogo):

                erros.append(regra.mensagem)

        return len(erros) == 0, erros
 
    def carregar_regras(

        self,

        arquivo

    ):

        arquivo = Path(arquivo)

        if not arquivo.exists():

            raise FileNotFoundError(

                arquivo

            )

        with open(

            arquivo,

            "r",

            encoding="utf8"

        ) as f:

            dados = json.load(f)

        for item in dados:

            self.regras.append(

                Rule(**item)

            )
 
if __name__ == "__main__":

    jogo = LotterySet([
        1,2,3,4,5,
        7,8,9,
        12,13,
        18,
        20,22,24,25
    ])

    validador = ValidatorEngine()

    ok, erros = validador.validar(jogo)

    print()

    print("Válido:", ok)

    print()

    if erros:

        print("Erros encontrados:")

        for erro in erros:

            print("-", erro)

    else:

        print("Nenhuma inconsistência encontrada.")



