import random
from collections import Counter
import matplotlib.pyplot as plt


def simular_soma_com_cores():
    numero_lancamentos = 1_000_000

    # 1. Gerar lançamentos e somas    dado1 = random.choices(range(1, 7), k=numero_lancamentos)
    dado2 = random.choices(range(1, 7), k=numero_lancamentos)
    somas = [d1 + d2 for d1, d2 in zip(dado1, dado2)]

    # 2. Contar as frequências (as somas vão de 2 a 12, totalizando 11 barras)
    frequencias = Counter(somas)
    valores_soma = list(range(2, 13))

    # 3. Converter para escala decimal dividindo pelo total
    contagens_decimais = [frequencias[soma] / numero_lancamentos for soma in valores_soma]

    # 4. Configurar estilo do Matplotlib
    try:
        plt.style.use('seaborn-v0_8-whitegrid')
    except:
        plt.style.use('ggplot')

    fig, ax = plt.subplots(figsize=(11, 6))

    # --- DESTAQUE: BAR COLORS ---
    # Como temos 11 barras (de 2 a 12), criamos uma lista com 11 cores.
    # Fizemos um efeito "espelhado", onde as bordas são mais frias (azul/roxo)
    # e o centro (soma 7) é uma cor mais forte.
    cores_personalizadas = [
        '#C2C2F0', '#99FF99', '#66B3FF', '#FFCC99', '#FF9999',
        '#FF5050',  # O 7 fica no centro (mais provável: ~0.1666)
        '#FF9999', '#FFCC99', '#66B3FF', '#99FF99', '#C2C2F0'
    ]

    # --- DESTAQUE: VARIÁVEL AX.BAR ---
    # Ao invés de apenas desenhar as barras, salvamos o retorno do comando
    # na variável 'bars'. Além disso, passamos nossa lista de cores no parâmetro 'color'.
    bars = ax.bar(valores_soma, contagens_decimais, color=cores_personalizadas,
                  edgecolor='#333333', linewidth=1.5, zorder=3, alpha=0.9)

    # Estilização de Textos e Grade
    ax.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)
    ax.set_title('Distribuição da Soma de 2 Dados (Escala Decimal)', fontsize=15, fontweight='bold', pad=20)
    ax.set_xlabel('Soma das Faces (Dado 1 + Dado 2)', fontsize=12, fontweight='bold', labelpad=10)
    ax.set_ylabel('Frequência Relativa', fontsize=12, fontweight='bold', labelpad=10)
    ax.set_xticks(valores_soma)
    ax.set_ylim(0, max(contagens_decimais) * 1.15)

    # --- USANDO A VARIÁVEL BARS ---
    # Agora iteramos sobre a variável 'bars' que criamos acima.
    # Isso permite extrair propriedades individuais de CADA barra, como altura (valor Y)
    # e posição (valor X), para colocar o texto de escala decimal perfeitamente alinhado no topo.
    for bar in bars:
        altura = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., altura + 0.003,
                f'{altura:.4f}',  # Formatado com 4 casas decimais para manter a beleza
                ha='center', va='bottom', fontsize=10, fontweight='bold', color='#2c3e50')

    # Limpeza visual minimalista
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Salvar o arquivo
    plt.tight_layout()
    plt.savefig('grafico_soma_cores_decimal.png', dpi=300)
    print("Gráfico em escala decimal gerado com sucesso!")


simular_soma_com_cores()