matriz = [[0, 0, 0],   # linha 0
          [0, 0, 0],   # linha 1
          [0, 0, 0]]   # linha 2

# leitura dos valores
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f"Valor para [{linha}, {coluna}]: "))

# impressão formatada
print("-=" * 20)
for linha in range(3):
    for coluna in range(3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
    print()
