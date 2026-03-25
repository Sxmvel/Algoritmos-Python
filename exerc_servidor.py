alertas_servidor = []

parar = "sim"

while parar != "nao":

    nome_servidor = input("Nome do servidor: ")
    tempo_resposta = input("Tempo de resposta: ")

    registro = (nome_servidor,tempo_resposta)

    alertas_servidor.append(registro)

    parar = input("Deseja fazer um novo registro sim/nao: ")

print("Aqui esta sua lista de registro: ", alertas_servidor)