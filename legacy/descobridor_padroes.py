import pandas as pd

ARQUIVO = "Analise_Historica_Lotofacil.xlsx"

df = pd.read_excel(
    ARQUIVO,
    sheet_name="Estatisticas_Concurso"
)

print()

print("===================================")
print("DESCOBRIDOR DE PADRÕES")
print("===================================")

print()

print("Total de concursos:", len(df))

print()

print("==============================")
print("PERFIS MAIS FREQUENTES")
print("==============================")

perfis = (
    df["perfil"]
    .value_counts()
    .reset_index()
)

perfis.columns = [
    "Perfil",
    "Quantidade"
]

perfis["Percentual"] = (
    perfis["Quantidade"]
    / len(df)
    *100
).round(2)

print(perfis.head(20))

print()

print("==============================")
print("PARES")
print("==============================")

print(

    df["Pares"]

    .value_counts()

    .sort_index()

)

print()

print("==============================")
print("BAIXAS")
print("==============================")

print(

    df["Baixas"]

    .value_counts()

    .sort_index()

)

print()

print("==============================")
print("CENTRO")
print("==============================")

print(

    df["Centro"]

    .value_counts()

    .sort_index()

)

print()

print("==============================")
print("MOLDURA")
print("==============================")

print(

    df["Moldura"]

    .value_counts()

    .sort_index()

)

print()

print(df["Centro"].describe())