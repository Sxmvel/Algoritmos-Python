lista_compras = []

# Condição inicial para garantir que o laço rode a primeira vez
resposta = "Sim"

while resposta != "Nao":
    item = input("Informe o item: ")
    lista_compras.append(item)

    # A última ação do laço define se ele vai repetir ou parar
    resposta = input("Deseja inserir mais itens (Sim/Nao)? ")


lista_compras.sort()



print("Sua lista de compras final: ", lista_compras)