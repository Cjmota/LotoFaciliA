import pandas as pd

import numpy as np


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

def analisar_pares(bolas):
    """
    Retorna:
        quantidade de pares
        quantidade de ímpares
    """

    pares = sum(
        1 for b in bolas
        if b % 2 == 0
    )

    impares = len(bolas) - pares

    return pares, impares

def analisar_consecutivos(bolas):
    """
    Conta ligações consecutivas.
    """

    consecutivos = 0

    for i in range(len(bolas)-1):

        if bolas[i+1] - bolas[i] == 1:
            consecutivos += 1

    return consecutivos

def analisar_linhas(bolas):
    """
    Retorna a quantidade de dezenas
    em cada linha do volante.
    """

    linhas = [0,0,0,0,0]

    for bola in bolas:

        linha = (bola - 1) // 5

        linhas[linha] += 1

    return tuple(linhas)

def analisar_colunas(bolas):
    """
    Retorna a quantidade de dezenas
    em cada coluna do volante.
    """

    colunas = [0, 0, 0, 0, 0]

    for bola in bolas:

        coluna = (bola - 1) % 5

        colunas[coluna] += 1

    return tuple(colunas)

def analisar_moldura_centro(bolas):

    CENTRO = {
        7,8,9,
        12,13,14,
        17,18,19
    }

    centro = sum(
        1 for b in bolas
        if b in CENTRO
    )

    moldura = len(bolas) - centro

    return moldura, centro

def faixa_soma(valor):

    inicio = (valor // 10) * 10

    fim = inicio + 9

    return f"{inicio}-{fim}"



print(f"Total de concursos: {TOTAL}")

#TESTE TESTE TESTE TESTE
teste = analisar_linhas(
    [1,2,4,5,7,8,11,13,15,16,18,20,22,23,25]
)

print()

print("TESTE LINHAS")

print(teste)


teste = analisar_colunas(
    [1,2,4,5,7,8,11,13,15,16,18,20,22,23,25]
)

print()

print("TESTE COLUNAS")

print(teste)


#TESTE TESTE TESTE TESTE


for _, linha in df.iterrows():

    bolas = sorted(
        int(linha[f"Bola{i}"])
        for i in range(1,16)
    )

    # -------------------------
    # PARES
    # -------------------------

    qtd_pares, qtd_impares = analisar_pares(bolas)

    pares[qtd_pares] = pares.get(qtd_pares,0)+1

    # -------------------------
    # SOMA
    # -------------------------

    soma = sum(bolas)

    faixa = faixa_soma(soma)
    
    somas[faixa] = somas.get(faixa,0)+1

    # -------------------------
    # BAIXAS
    # -------------------------

    qtd_baixas = sum(
        1 for b in bolas
        if b <= 13
    )

    baixas[qtd_baixas] = baixas.get(qtd_baixas,0)+1

    # -------------------------
    # ALTAS
    # -------------------------

    qtd_altas = 15 - qtd_baixas

    altas[qtd_altas] = altas.get(qtd_altas,0)+1
    
    # -------------------------
    # CONSECUTIVOS
    # -------------------------

    consecutivos = 0

    consecutivos = analisar_consecutivos(bolas)
                    
    #ATUALIZA CONSECUTIVOS
    consecutivos_hist[consecutivos] = (
        consecutivos_hist.get(consecutivos,0) + 1
    )
    
    # -------------------------
    # LINHAS E COLUNAS
    # -------------------------

    linhas = analisar_linhas(bolas)

    colunas = analisar_colunas(bolas)
    
    moldura, centro = analisar_moldura_centro(bolas)
    
    # ============================
    # HISTÓRICO DAS LINHAS
    # ============================

    linhas_hist[linhas] = (
        linhas_hist.get(linhas,0) + 1
    )

    # ============================
    # HISTÓRICO DAS COLUNAS
    # ============================

    colunas_hist[colunas] = (
        colunas_hist.get(colunas,0) + 1
    )

    # ============================
    # HISTÓRICO DO CENTRO
    # ============================

    centro_hist[centro] = (
        centro_hist.get(centro,0) + 1
    )

    # ============================
    # HISTÓRICO DA MOLDURA
    # ============================

    moldura_hist[moldura] = (
        moldura_hist.get(moldura,0) + 1
    )
    
    # -------------------------
    # PERFIL ESTATÍSTICO
    # -------------------------

    perfil = (
        f"P{qtd_pares}"
        f"-B{qtd_baixas}"
        f"-C{consecutivos}"
        f"-L{''.join(map(str, linhas))}"
        f"-CO{''.join(map(str, colunas))}"
        f"-M{moldura}"
        f"-CT{centro}"
    )
    
    estatisticas.append({

        "Concurso": int(linha["Concurso"]),

        "Pares": qtd_pares,

        "Impares": qtd_impares,

        "Soma": soma,

        "Baixas": qtd_baixas,

        "Altas": qtd_altas,

        "Consecutivos": consecutivos,
        
        "perfil": perfil,
        
        "faixa_soma" : faixa,
        
        "L1": linhas[0],
        "L2": linhas[1],
        "L3": linhas[2],
        "L4": linhas[3],
        "L5": linhas[4],

        "C1": colunas[0],
        "C2": colunas[1],
        "C3": colunas[2],
        "C4": colunas[3],
        "C5": colunas[4],
        
        "Moldura": moldura,
        "Centro": centro

    })
    
    perfis[perfil] = perfis.get(perfil,0) + 1
    
    
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

print()

print("==============================")
print(" MENOR SOMA")
print("==============================")

print(min(somas))

print()

print("==============================")
print(" MAIOR SOMA")
print("==============================")

print(max(somas))

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

df_somas = criar_dataframe_distribuicao(
    somas,
    "Soma",
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

#df_perfis.head(20)


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

    df_somas.to_excel(
        writer,
        sheet_name="Somas",
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