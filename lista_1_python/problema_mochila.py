itens = [
    {'id': 1, 'w': 2, 'v': 10}, {'id': 2, 'w': 3, 'v': 20},
    {'id': 3, 'w': 4, 'v': 30}, {'id': 4, 'w': 5, 'v': 40},
    {'id': 5, 'w': 9, 'v': 50}
]
capacidade = 15

# Heurística: Ordenar pela razão Valor/Peso
itens_ordenados = sorted(itens, key=lambda x: x['v']/x['w'], reverse=True)

mochila = []
peso_atual = 0
valor_total = 0

for item in itens_ordenados:
    if peso_atual + item['w'] <= capacidade:
        mochila.append(item['id'])
        peso_atual += item['w']
        valor_total += item['v']

print(f"Itens na mochila: {mochila}")
print(f"Peso Total: {peso_atual}kg | Valor Total: ${valor_total}")