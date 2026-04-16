def heuristica_gulosa_mochila(capacidade, pesos, valores):
    # 1. Cria uma estrutura para armazenar os itens com sua Razão (Valor/Peso)
    itens = []
    for i in range(len(pesos)):
        razao = valores[i] / pesos[i]
        itens.append({
            'id': i + 1,
            'peso': pesos[i],
            'valor': valores[i],
            'razao': razao
        })

    # 2. Ordena os itens pela razão de forma decrescente (do mais vantajoso pro menos)
    itens.sort(key=lambda x: x['razao'], reverse=True)

    mochila = []
    peso_total = 0
    valor_total = 0

    print(f"Capacidade máxima da mochila: {capacidade}\n")
    print("--- Itens Ordenados (Heurística Gulosa) ---")
    for item in itens:
        print(f"Item {item['id']}: Peso={item['peso']}, Valor={item['valor']}, Razão={item['razao']:.4f}")

    print("\n--- Preenchendo a Mochila ---")

    # 3. Tenta colocar cada item na mochila seguindo a ordem de prioridade
    for item in itens:
        if peso_total + item['peso'] <= capacidade:
            mochila.append(item['id'])
            peso_total += item['peso']
            valor_total += item['valor']
            print(f"[OK] Item {item['id']} adicionado. Espaço ocupado: {peso_total:.2f}/{capacidade}")
        else:
            espaco_restante = capacidade - peso_total
            print(f"[X]  Item {item['id']} rejeitado. Peso {item['peso']} > Espaço restante {espaco_restante:.2f}")

    return mochila, peso_total, valor_total


# --- Dados do Problema ---
capacidade_mochila = 23
pesos_itens = [5.2, 2.7, 7, 7.5, 6.1, 4.3, 3.1]
valores_itens = [5, 7, 10, 10, 9, 9.5, 4.9]

# Executa o algoritmo
itens_selecionados, peso_final, valor_final = heuristica_gulosa_mochila(capacidade_mochila, pesos_itens, valores_itens)

# --- Exibe os Resultados Finais ---
print("\n--- Resultado Final ---")
print(f"Itens selecionados: {itens_selecionados}")
print(f"Peso total ocupado: {peso_final:.2f}")
print(f"Valor total obtido: {valor_final:.2f}")