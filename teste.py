todas_equipes = []


continuar = "s"

while continuar != "n":
    nome_equipe = input("Informe o nome da equipe: ")
    problemas = int(input("informe a quantidade de problemas resolvidos: "))
    info_equipe = [nome_equipe, problemas]
    todas_equipes.append(info_equipe)
    continuar = input("Registrar outra equipe? (s/n): ")

print(todas_equipes)