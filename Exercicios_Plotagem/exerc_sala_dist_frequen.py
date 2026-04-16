import random
from collections import Counter


def simular_dados():

    numero_lancamentos = 1_000_000

    # Gera 1 milhão de lançamentos com valores de 1 a 6 de forma otimizada
    lancamentos = random.choices(range(1, 7), k=numero_lancamentos)

    # Conta a frequência de cada face
    frequencias = Counter(lancamentos)

    # Exibe os resultados ordenados pela face do dado
    print(f"Resultados de {numero_lancamentos} lançamentos:\n")
    for face in range(1, 7):
        # frequencias[face] pega a quantidade de vezes que o número saiu
        print(f"face {face} apareceu {frequencias[face]} vezes")


# Executa a função
simular_dados()