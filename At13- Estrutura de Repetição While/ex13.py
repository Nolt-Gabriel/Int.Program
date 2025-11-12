soma = 0
cont = 0
maior = menor = None

continuar = 'S'
while continuar in 'Ss':
    num = int(input("Digite um número: "))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = input("Quer continuar? [S/N] ").strip().upper()

media = soma / cont if cont > 0 else 0
print(f"Foram digitados {cont} números.")
print(f"A média entre todos é {media}.")
print(f"O maior valor foi {maior} e o menor foi {menor}.")
