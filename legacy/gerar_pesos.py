import pandas as pd
import json


def normalizar_chave(valor) -> str:

    if isinstance(valor, float) and valor.is_integer():

        return str(int(valor))

    return str(valor)

def criar_registro(linha) -> dict:

    return {

        "probabilidade": float(linha["Probabilidade"]),

        "peso_bayes": float(linha["Peso_Bayes"]),

        "percentual": float(linha["Percentual"]),

        "ranking": int(linha["Ranking"]),

        "quantidade": int(linha["Quantidade"]),

        "nota": float(linha.get("Nota", 0))

    }

ARQUIVO = "Analise_Historica_Lotofacil.xlsx"

xls = pd.ExcelFile(ARQUIVO)

ABAS = xls.sheet_names

for aba in ABAS:

    df = pd.read_excel(
        xls,
        sheet_name=aba
    )


pesos_json = {}

#writer = pd.ExcelWriter("pesos_estatisticos.xlsx")
with pd.ExcelWriter("pesos_estatisticos.xlsx") as writer:

    for aba in ABAS:

        df = pd.read_excel(
            ARQUIVO,
            sheet_name=aba
        )
        

        df.to_excel(
            writer,
            sheet_name=aba,
            index=False
        )

        coluna_valor = df.columns[0]

        pesos_json[aba] = {}

        for _, linha in df.iterrows():

            chave = normalizar_chave(linha[coluna_valor])

            pesos_json[aba][chave] = criar_registro(linha)


with open(
    "pesos_estatisticos.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(
        pesos_json,
        f,
        indent=4,
        ensure_ascii=False
    )

print()

print("==========================")
print("PESOS GERADOS")
print("==========================")

print()

print("Excel : pesos_estatisticos.xlsx")

print("JSON  : pesos_estatisticos.json")