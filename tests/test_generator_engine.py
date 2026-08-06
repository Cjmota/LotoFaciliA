from engine.generator_engine import  GeneratorEngine

generator = GeneratorEngine()

game = generator.gerar([
    
    1, 2, 3, 4, 5,
    7, 8, 9,
    12, 13,
    18,
    20, 22, 24, 25
    
])

print()

print("=" * 40)
print("GAME")
print("=" * 40)
print(game)

print()

print("=" * 40)
print("ESTATÍSTICAS")
print("=" * 40)

for nome, valor in game.estatisticas.items():
    print(f"{nome:<22}: {valor}")

print()

print("=" * 40)
print("SCORE")
print("=" * 40)
print(game.score)

print()

print("=" * 40)
print("VALIDAÇÃO")
print("=" * 40)
print(game.valido)

print()

print("=" * 40)
print("ERROS")
print("=" * 40)
print(game.erros)

