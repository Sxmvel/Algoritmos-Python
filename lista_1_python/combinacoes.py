combinacoes = []
for r in range(1, len(conjunto) + 1):
    combinacoes.extend(list(itertools.combinations(conjunto, r)))

print(f"Total de combinações (subconjuntos): {len(combinacoes)}") # 2^5 - 1 = 31
# Exemplo:
for c in combinacoes[:5]:
    print(c)