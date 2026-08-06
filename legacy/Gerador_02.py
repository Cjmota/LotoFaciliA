import pandas as pd
import random

# ===== CONFIGURAÇÕES =====
ARQUIVO_ESTATISTICAS = "estatisticas_lotofacil.xlsx"
TOTAL_NUMEROS = list(range(1, 26))
NUMEROS_POR_JOGO = 15
NUM_JOGOS = 100

MIN_QUENTES = 5
MIN_FRIOS = 5
MAX_MEIO = NUMEROS_POR_JOGO - MIN_QUENTES - MIN_FRIOS
ESTRATEGIA = 'equilibrado'  # 'equilibrado', 'mais_quentes', 'mais_frios'

# ===== PESOS DA AVALIAÇÃO =====
PESO_FREQ = 0.70
PESO_ATRASO = 0.30

# ===== CARREGAR ESTATÍSTICAS =====
df = pd.read_excel(ARQUIVO_ESTATISTICAS)

# Índice para acesso rápido aos dados
dados = df.set_index("Número")

# ===== CARREGAR ESTATÍSTICAS =====
df = pd.read_excel(ARQUIVO_ESTATISTICAS)

# ==========================
# NORMALIZAÇÃO DAS ESTATÍSTICAS
# ==========================

# Frequência (0 até 1)
freq_min = df["Frequência"].min()
freq_max = df["Frequência"].max()

df["Freq_Norm"] = (
    (df["Frequência"] - freq_min)
    /
    (freq_max - freq_min)
)

# Atraso (0 até 1)
atraso_min = df["Atraso Atual"].min()
atraso_max = df["Atraso Atual"].max()

if atraso_max == atraso_min:
    df["Atraso_Norm"] = 0
else:
    df["Atraso_Norm"] = (
        (df["Atraso Atual"] - atraso_min)
        /
        (atraso_max - atraso_min)
    )


# Listas
# 15 números mais frequentes
quentes = (
    df.sort_values("Frequência", ascending=False)["Número"]
      .tolist()[:15]
)

# 15 números mais atrasados
frios = (
    df.sort_values("Atraso Atual", ascending=False)["Número"]
      .tolist()[:15]
)

# Demais números
medios = [
    n for n in TOTAL_NUMEROS
    if n not in quentes and n not in frios
]

# ===== FUNÇÃO DE PONTUAÇÃO =====
def avaliar_jogo(jogo):

    nota = 0

    for numero in jogo:

        linha = dados.loc[numero]

        nota += (
            linha["Freq_Norm"] * PESO_FREQ
            +
            linha["Atraso_Norm"] * PESO_ATRASO
        )

    return round(nota * 100, 2)

# ===== GERAR UM JOGO OTIMIZADO =====
def gerar_jogo_otimizado(quentes_disponiveis, frios_disponiveis, medios_disponiveis):
    k_quentes = min(MIN_QUENTES, len(quentes_disponiveis))
    k_frios = min(MIN_FRIOS, len(frios_disponiveis))
    selecionados_quentes = set(random.sample(quentes_disponiveis, k=k_quentes))
    selecionados_frios = set(random.sample(frios_disponiveis, k=k_frios))

    # Selecionar do meio
    k_meio = NUMEROS_POR_JOGO - len(selecionados_quentes.union(selecionados_frios))
    k_meio = min(k_meio, len(medios_disponiveis))
    selecionados_meio = set(random.sample(medios_disponiveis, k=k_meio))

    jogo = selecionados_quentes.union(selecionados_frios).union(selecionados_meio)

    # Completar caso falte algum número
    while len(jogo) < NUMEROS_POR_JOGO:
        jogo.add(random.choice([n for n in TOTAL_NUMEROS if n not in jogo]))

    return tuple(sorted(jogo)), selecionados_quentes, selecionados_frios, selecionados_meio

# ===== GERAR TODOS OS JOGOS =====
todos_jogos = []
quentes_usados = set()
frios_usados = set()
medios_usados = set()
tentativas = 0
max_tentativas = NUM_JOGOS * 10

while len(todos_jogos) < NUM_JOGOS and tentativas < max_tentativas:
    quentes_disp = [n for n in quentes[:15] if n not in quentes_usados]
    frios_disp = [n for n in frios[:15] if n not in frios_usados]
    medios_disp = [n for n in medios if n not in medios_usados]

    # Reiniciar cobertura se necessário
    if len(quentes_disp) < MIN_QUENTES:
        quentes_disp = quentes[:15]
        quentes_usados = set()
    if len(frios_disp) < MIN_FRIOS:
        frios_disp = frios[:15]
        frios_usados = set()
    if len(medios_disp) < MAX_MEIO:
        medios_disp = medios
        medios_usados = set()

    novo_jogo, q_j, f_j, m_j = gerar_jogo_otimizado(quentes_disp, frios_disp, medios_disp)

    if novo_jogo not in todos_jogos:
        todos_jogos.append(novo_jogo)
        quentes_usados.update(q_j)
        frios_usados.update(f_j)
        medios_usados.update(m_j)

    tentativas += 1

# ===== PONTUAÇÃO E ESTIMATIVA DE ACERTOS =====

def estimativa_acertos(jogo):
    frequencias = [df.loc[df["Número"] == n, "Frequência"].values[0] for
                   n in jogo] 
    total_concursos = df["Último Concurso"].max() 
    prob_acerto = [f / total_concursos for f in frequencias] 

    # Simular probabilidade de 11,12,13,14,15 acertos combinando probabilidades individuais 
    # Simplificação: soma das médias ponderadas 
    media_prob = sum(prob_acerto)/len(prob_acerto) 
    est_11 = round(media_prob * 11, 2) 
    est_12 = round(media_prob * 12, 2) 
    est_13 = round(media_prob * 13, 2) 
    est_14 = round(media_prob * 14, 2) 
    est_15 = round(media_prob * 15, 2) 
    return est_11, est_12, est_13, est_14, est_15

pontuacoes = [avaliar_jogo(j) for j in todos_jogos]

print()

print("TOP 10 JOGOS")

for i, jogo in enumerate(todos_jogos[:10]):

    print()

    print(jogo)

    print("Nota:", pontuacoes[i])

estimativas = [estimativa_acertos(j) for j in todos_jogos]

# ===== EXPORTAR PARA EXCEL =====
jogos_df = pd.DataFrame(list(todos_jogos), columns=[f"Bola{i}" for i in range(1, NUMEROS_POR_JOGO+1)])
jogos_df["Pontuacao_Esperada"] = pontuacoes
jogos_df["Est_11"] = [e[0] for e in estimativas]
jogos_df["Est_12"] = [e[1] for e in estimativas]
jogos_df["Est_13"] = [e[2] for e in estimativas]
jogos_df["Est_14"] = [e[3] for e in estimativas]
jogos_df["Est_15"] = [e[4] for e in estimativas]

jogos_df.index += 1
saida_excel = f"Jogos_do_Gerador_01_{NUM_JOGOS}_jogos.xlsx"
jogos_df.to_excel(saida_excel, index_label="Jogo")


print(f"🎯 {len(todos_jogos)} Jogos do Gerador_01 gerados com sucesso!")
print(f"📁 Arquivo Excel salvo: {saida_excel}")
print("\nPrimeiros 5 jogos:")
print(jogos_df.head())
