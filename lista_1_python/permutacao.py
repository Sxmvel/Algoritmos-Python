import itertools

conjunto = ['a', 'b', 'c', 'd', 'e']
permutacoes = list(itertools.permutations(conjunto))

print(f"Total de permutações: {len(permutacoes)}")
for p in permutacoes[:5]:
    print(p)