maior = 0
menor = 0

for i in range(5):
    peso = float(input(f"Digite o peso da pessoa {i+1} (em kg): "))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior peso lido foi {maior} kg.")
print(f"O menor peso lido foi {menor} kg.")
