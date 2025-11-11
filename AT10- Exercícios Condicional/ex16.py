a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a <= b and a <= c:
    menor = a
    if b <= c:
        meio = b
        maior = c
    else:
        meio = c
        maior = b
elif b <= a and b <= c:
    menor = b
    if a <= c:
        meio = a
        maior = c
    else:
        meio = c
        maior = a
else:
    menor = c
    if a <= b:
        meio = a
        maior = b
    else:
        meio = b
        maior = a

print(f'Ordem crescente: {menor}, {meio}, {maior}')
