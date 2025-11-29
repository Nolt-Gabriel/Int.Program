matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

soma_pares = 0
soma_terceira_coluna = 0

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f"Valor para [{linha}, {coluna}]: "))
        valor = matriz[linha][coluna]

        
        if valor % 2 == 0:
            soma_pares += valor

        
        if coluna == 2:
            soma_terceira_coluna += valor


print("-=" * 20)
for linha in range(3):
    for coluna in range(3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
    print()


maior_segunda_linha = max(matriz[1])

print(f"A) Soma dos valores pares: {soma_pares}")
print(f"B) Soma dos valores da terceira coluna: {soma_terceira_coluna}")
print(f"C) Maior valor da segunda linha: {maior_segunda_linha}")
