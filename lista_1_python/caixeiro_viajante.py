# Função de leitura sugerida no exercício
def le_distancias_tsp(arquivo, n_cidades=50):
    # Assume-se que o arquivo contém a matriz de distâncias flat ou lista de arestas
    dist_matrix = np.zeros((n_cidades, n_cidades))
    return dist_matrix


# Exercício 5: Vizinho Mais Próximo (Caminho mais curto)
def tsp_vizinho_proximo(dist_matrix, inicio=9):  # cidade 10 é índice 9
    n = len(dist_matrix)
    visitados = [False] * n
    rota = [inicio]
    visitados[inicio] = True
    distancia_total = 0

    atual = inicio
    for _ in range(n - 1):
        proximo = -1
        menor_dist = float('inf')
        for i in range(n):
            if not visitados[i] and dist_matrix[atual][i] < menor_dist:
                menor_dist = dist_matrix[atual][i]
                proximo = i
        rota.append(proximo)
        visitados[proximo] = True
        distancia_total += menor_dist
        atual = proximo

    distancia_total += dist_matrix[atual][inicio]  # Volta ao início
    return rota, distancia_total

