matriz = []

for i in range (2):
    matriz.append([])
    for j in range(2):
        valor = int(input("valor: "))
        matriz[i].append(valor)


print(matriz)


print("Matriz 2x2")

for i in range(len(matriz)):
    print(matriz[i])