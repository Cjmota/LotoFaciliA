import json

with open(
    "pesos_estatisticos.json",
    encoding="utf8"
) as f:

    pesos = json.load(f)

print()

print("========================")

print("PESOS CARREGADOS")

print("========================")

print()

for categoria in pesos:

    print(categoria)

    print(pesos[categoria])

    print()