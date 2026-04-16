lista_compras = []

resposta = "Sim"

while resposta != "Nao":

    item = input("Informe o item: ")


    qtde = float(input("Informe a quantidade: "))

    # 3. Cria a Tupla (o "pacote" fechado com os dois valores)
    item_compra = (item, qtde)


    lista_compras.append(item_compra)

    # Pergunta se quer continuar
    resposta = input("Deseja inserir mais itens? (Sim/Nao): ")

print("Sua lista de compras final: ", lista_compras)