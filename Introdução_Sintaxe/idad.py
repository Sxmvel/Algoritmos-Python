idade_texto = input("Digite a sua idade: ")
idade = int(idade_texto)


if idade >= 18:
    print("Você já é maior")
else:
    falta = 18 - idade
    print("Ainda falta ", falta ," anos para você fazer 18")

