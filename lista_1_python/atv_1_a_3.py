import numpy as np
import matplotlib.pyplot as plt

# Semente para reprodutibilidade (conforme solicitado no notebook)
np.random.seed(1000)

def exercicio_1():
    lancamentos = np.random.randint(1, 7, size=1000000)
    faces, frequencias = np.unique(lancamentos, return_counts=True)

    plt.bar(faces, frequencias, color='skyblue', edgecolor='black')
    plt.title('Distribuição de Frequência - 1 Dado (1.000.000 lançamentos)')
    plt.xlabel('Face do Dado')
    plt.ylabel('Frequência')
    plt.xticks(faces)
    plt.show()

exercicio_1()


def exercicio_2():
    dado1 = np.random.randint(1, 7, size=1000000)
    dado2 = np.random.randint(1, 7, size=1000000)
    somas = dado1 + dado2

    faces_soma, frequencias = np.unique(somas, return_counts=True)

    plt.bar(faces_soma, frequencias, color='salmon', edgecolor='black')
    plt.title('Distribuição da Soma de 2 Dados')
    plt.xlabel('Soma das Faces')
    plt.ylabel('Frequência')
    plt.xticks(faces_soma)
    plt.show()


exercicio_2()


def simular_dados_generico(qtd_dados, num_lancamentos):
    # Gera uma matriz (lançamentos x dados) e soma as colunas
    lancamentos = np.random.randint(1, 7, size=(num_lancamentos, qtd_dados))
    somas = np.sum(lancamentos, axis=1)

    valores, frequencias = np.unique(somas, return_counts=True)

    plt.figure(figsize=(10, 6))
    plt.bar(valores, frequencias, color='lightgreen', edgecolor='black')
    plt.title(f'Soma de {qtd_dados} Dados - {num_lancamentos} Lançamentos')
    plt.xlabel('Soma')
    plt.ylabel('Frequência')
    plt.show()


simular_dados_generico(3, 1000000)