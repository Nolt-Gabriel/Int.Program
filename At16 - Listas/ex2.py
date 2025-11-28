numeros = []

while True:
    n = int(input("Digite um valor: "))

    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Não será adicionado.")

    continuar = input("Quer continuar? [S/N] ").strip().upper()
    if continuar == "N":
        break

numeros.sort()
print("Valores únicos em ordem crescente:", numeros)
