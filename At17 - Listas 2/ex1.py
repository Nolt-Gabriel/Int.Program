pessoas = []
maior = menor = 0

while True:
    nome = input("Nome: ")
    peso = float(input("Peso: "))

    pessoas.append([nome, peso])

    if len(pessoas) == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    op = input("Quer continuar? [S/N] ").strip().upper()
    if op == "N":
        break

print("-=" * 20)
print(f"A) Foram cadastradas {len(pessoas)} pessoas.")

print(f"B) Maior peso foi {maior} kg. Pessoas com esse peso: ", end="")
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=" ")
print()

print(f"C) Menor peso foi {menor} kg. Pessoas com esse peso: ", end="")
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=" ")
print()
