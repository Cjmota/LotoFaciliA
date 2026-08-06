import json
from pathlib import Path

import pandas as pd


class ValidatorRuleGenerator:

    ABAS = {
        "Pares": "pares",
        "Baixas": "baixas",
        "Centro": "centro",
        "Moldura": "moldura",
        "Consecutivos": "consecutivos",
        "Primos": "primos",
        "Fibonacci": "fibonacci",
        "Multiplos3": "multiplos3"
    }

    def __init__(
        self,
        arquivo_excel="Analise_Historica_Lotofacil.xlsx",
        arquivo_saida="validator_rules.json",
        confianca=95
    ):

        self.arquivo_excel = Path(arquivo_excel)
        self.arquivo_saida = Path(arquivo_saida)
        self.confianca = confianca

    # ===========================================================
    # LEITURA
    # ===========================================================

    def ler_aba(self, nome):

        return pd.read_excel(
            self.arquivo_excel,
            sheet_name=nome
        )

    # ===========================================================
    # DESCOBRE O INTERVALO MAIS PROVÁVEL
    # ===========================================================

    def descobrir_intervalo(self, df, coluna):

        if "Quantidade" not in df.columns:
            raise ValueError("Coluna 'Quantidade' não encontrada.")

        if "Percentual" not in df.columns:
            raise ValueError("Coluna 'Percentual' não encontrada.")

        df = df.sort_values(
            by="Quantidade",
            ascending=False
        )

        acumulado = 0

        valores = []

        for _, linha in df.iterrows():

            acumulado += linha["Percentual"]

            valores.append(linha[coluna])

            if acumulado >= self.confianca:
                break

        return min(valores), max(valores)

    # ===========================================================
    # GERA UMA REGRA
    # ===========================================================

    def criar_regra(
        self,
        nome,
        atributo,
        minimo,
        maximo
    ):

        return {

            "nome": nome,

            "atributo": atributo,

            "minimo": int(minimo),

            "maximo": int(maximo),

            "mensagem": f"{nome} fora do padrão"

        }

    # ===========================================================
    # GERA TODAS AS REGRAS
    # ===========================================================

    def gerar(self):

        regras = []

        print()
        print("=" * 60)
        print("GERANDO REGRAS AUTOMÁTICAS")
        print("=" * 60)

        for aba, atributo in self.ABAS.items():

            df = self.ler_aba(aba)

            coluna = df.columns[0]

            minimo, maximo = self.descobrir_intervalo(
                df,
                coluna
            )

            regra = self.criar_regra(
                aba,
                atributo,
                minimo,
                maximo
            )

            regras.append(regra)

            print(
                f"{aba:<15} {minimo} -> {maximo}"
            )

        with open(
            self.arquivo_saida,
            "w",
            encoding="utf8"
        ) as f:

            json.dump(
                regras,
                f,
                indent=4,
                ensure_ascii=False
            )

        print()
        print(f"Arquivo criado: {self.arquivo_saida}")


if __name__ == "__main__":

    g = ValidatorRuleGenerator(
        confianca=95
    )

    g.gerar()