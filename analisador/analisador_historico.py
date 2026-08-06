import pandas as pd

import numpy as np

from engine.feature_engine import extrair_features


ARQUIVO = "lotofacil.xlsx"

df = pd.read_excel(ARQUIVO)

TOTAL = len(df)

# Armazena todas as estatísticas por concurso
estatisticas = []

# ===========================
# DICIONÁRIOS
# ===========================

pares = {}
somas = {}
baixas = {}
altas = {}

consecutivos_hist = {}

centro_hist = {}

moldura_hist = {}

linhas_hist = {}

colunas_hist = {}

perfis = {}


def criar_dataframe_distribuicao(dicionario, nome_coluna, total):

    df = pd.DataFrame(
        [
            {
                nome_coluna: chave,
                "Quantidade": valor
            }
            for chave, valor in dicionario.items()
        ]
    )

    df = df.sort_values(
        by="Quantidade",
        ascending=False
    ).reset_index(drop=True)

    df["Ranking"] = df.index + 1

    df["Percentual"] = (
        df["Quantidade"] / total * 100
    ).round(2)

    df["Probabilidade"] = (
        df["Quantidade"] / total
    ).round(6)

    df["Peso_Bayes"] = (
        -np.log(df["Probabilidade"])
    ).round(6)

    df["Freq_Relativa"] = (
        df["Quantidade"]
        /
        df["Quantidade"].max()
    ).round(6)

    df["Percentual Acumulado"] = (
        df["Percentual"]
        .cumsum()
        .round(2)
    )

    return df

# =====================================================
# ANALISADORES
# =====================================================

print(f"Total de concursos: {TOTAL}")


for _, linha in df.iterrows():

    bolas = sorted(
        int(linha[f"Bola{i}"])
        for i in range(1, 16)
    )

    # =====================================
    # EXTRAI TODAS AS FEATURES DO JOGO
    # =====================================

    features = extrair_features(bolas)

    # =====================================
    # HISTÓRICOS
    # =====================================

    pares[features.pares] = pares.get(features.pares, 0) + 1

    baixas[features.baixas] = baixas.get(features.baixas, 0) + 1

    altas[features.altas] = altas.get(features.altas, 0) + 1

    somas[features.faixa_soma] = (
        somas.get(features.faixa_soma, 0) + 1
    )

    consecutivos_hist[features.consecutivos] = (
        consecutivos_hist.get(features.consecutivos, 0) + 1
    )

    linhas_hist[features.linhas] = (
        linhas_hist.get(features.linhas, 0) + 1
    )

    colunas_hist[features.colunas] = (
        colunas_hist.get(features.colunas, 0) + 1
    )

    centro_hist[features.centro] = (
        centro_hist.get(features.centro, 0) + 1
    )

    moldura_hist[features.moldura] = (
        moldura_hist.get(features.moldura, 0) + 1
    )

    # =====================================
    # PERFIL
    # =====================================

    perfil = (
        f"P{features.pares}"
        f"-B{features.baixas}"
        f"-C{features.consecutivos}"
        f"-FS{features.faixa_soma}"
        f"-L{''.join(map(str, features.linhas))}"
        f"-CO{''.join(map(str, features.colunas))}"
        f"-M{features.moldura}"
        f"-CT{features.centro}"
    )

    perfis[perfil] = perfis.get(perfil, 0) + 1

    # =====================================
    # ESTATÍSTICAS DO CONCURSO
    # =====================================

    estatisticas.append({

        "Concurso": int(linha["Concurso"]),
        
        **features.__dict__,
        
        "Perfil": perfil,
        
        "Jogo": "-".join(
            map(
                lambda x: f"{x:02d}",
                bolas
            )
        ),
        
        "Quantidade_Dezenas": len(bolas),

        "Pares": features.pares,
        "Impares": features.impares,

        "Baixas": features.baixas,
        "Altas": features.altas,

        "Soma": features.soma,
        "Faixa_Soma": features.faixa_soma,

        "Consecutivos": features.consecutivos,

        "L1": features.linhas[0],
        "L2": features.linhas[1],
        "L3": features.linhas[2],
        "L4": features.linhas[3],
        "L5": features.linhas[4],

        "C1": features.colunas[0],
        "C2": features.colunas[1],
        "C3": features.colunas[2],
        "C4": features.colunas[3],
        "C5": features.colunas[4],

        "Centro": features.centro,
        "Moldura": features.moldura

    })
        
    
print()

print("==============================")
print(" DISTRIBUIÇÃO DE CONSECUTIVOS")
print("==============================")

for k in sorted(consecutivos_hist):

    print(
        f"{k:2d} consecutivos -> "
        f"{consecutivos_hist[k]:4d} concursos "
        f"({consecutivos_hist[k]/TOTAL*100:.2f}%)"
    )

print()

print("==============================")
print(" DISTRIBUIÇÃO DE PARES")
print("==============================")

for k in sorted(pares):

    print(
        f"{k:2d} pares -> "
        f"{pares[k]:4d} concursos "
        f"({pares[k]/TOTAL*100:.2f}%)"
    )

print()

print("==============================")
print(" DISTRIBUIÇÃO BAIXAS")
print("==============================")

for k in sorted(baixas):

    print(
        f"{k:2d} baixas -> "
        f"{baixas[k]:4d} concursos "
        f"({baixas[k]/TOTAL*100:.2f}%)"
    )


# =====================================
# DATAFRAME - DISTRIBUIÇÃO DE PARES
# =====================================

df_pares = criar_dataframe_distribuicao(
    pares,
    "Pares",
    TOTAL
)

# =====================================
# DATAFRAME - DISTRIBUIÇÃO DE BAIXAS
# =====================================

df_baixas = criar_dataframe_distribuicao(
    baixas,
    "Baixas",
    TOTAL
)

# =====================================
# DATAFRAME - CONSECUTIVOS
# =====================================

df_consecutivos = criar_dataframe_distribuicao(
    consecutivos_hist,
    "Consecutivos",
    TOTAL
)

# =====================================
# DATAFRAME - SOMAS
# =====================================

df_faixas_somas = criar_dataframe_distribuicao(
    somas,
    "Faixa_Soma",
    TOTAL
)

df_perfis = criar_dataframe_distribuicao(
    perfis,
    "Perfil",
    TOTAL
)

df_linhas = criar_dataframe_distribuicao(
    linhas_hist,
    "Linhas",
    TOTAL
)

df_colunas = criar_dataframe_distribuicao(
    colunas_hist,
    "Colunas",
    TOTAL
)

df_centro = criar_dataframe_distribuicao(
    centro_hist,
    "Centro",
    TOTAL
)

df_moldura = criar_dataframe_distribuicao(
    moldura_hist,
    "Moldura",
    TOTAL
)


print()

print("Gerando arquivo estatístico...")

resultado = pd.DataFrame(estatisticas)

with pd.ExcelWriter("Analise_Historica_Lotofacil.xlsx") as writer:

    resultado.to_excel(
        writer,
        sheet_name="Estatisticas_Concurso",
        index=False
    )

    df_pares.to_excel(
        writer,
        sheet_name="Pares",
        index=False
    )

    df_baixas.to_excel(
        writer,
        sheet_name="Baixas",
        index=False
    )

    df_consecutivos.to_excel(
        writer,
        sheet_name="Consecutivos",
        index=False
    )

    df_faixas_somas.to_excel(
        writer,
        sheet_name="Faixa_Soma",
        index=False
    )
    
    df_perfis.to_excel(
        writer,
        sheet_name="Perfis",
        index=False
    )
    
    df_linhas.to_excel(
    writer,
    sheet_name="Linhas",
    index=False
    )

    df_colunas.to_excel(
        writer,
        sheet_name="Colunas",
        index=False
    )

    df_centro.to_excel(
        writer,
        sheet_name="Centro",
        index=False
    )

    df_moldura.to_excel(
        writer,
        sheet_name="Moldura",
        index=False
    )

print()

print("=====================================")
print("ANÁLISE CONCLUÍDA")
print("=====================================")

print()

print("Arquivo criado:")

print("Analise_Historica_Lotofacil.xlsx")