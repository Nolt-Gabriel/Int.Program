numeros = []
pares = []
impares = []

while True:
    n = int(input("Digite um número: "))
    numeros.append(n)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    op = input("Quer continuar? [S/N] ").strip().upper()
    if op == "N":
        break

print(f"Lista completa: {numeros}")
print(f"Lista de pares: {pares}")
print(f"Lista de ímpares: {impares}")
