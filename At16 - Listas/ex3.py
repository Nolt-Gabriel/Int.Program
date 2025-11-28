numeros = []

for i in range(5):
    n = int(input("Digite um valor: "))

    if i == 0 or n >= numeros[-1]:

        numeros.append(n)
        
    else:
        
        pos = 0
        while pos < len(numeros) and n > numeros[pos]:
            pos += 1
        numeros.insert(pos, n)

print("Lista ordenada:", numeros)
