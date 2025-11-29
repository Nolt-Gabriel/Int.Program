numeros = [[], []]   # numeros[0] = pares, numeros[1] = ímpares

for i in range(7):
    n = int(input(f"Digite o {i+1}º valor: "))
    if n % 2 == 0:
        numeros[0].append(n)   # pares
    else:
        numeros[1].append(n)   # ímpares

numeros[0].sort()
numeros[1].sort()

print(f"Pares em ordem crescente: {numeros[0]}")
print(f"Ímpares em ordem crescente: {numeros[1]}")
