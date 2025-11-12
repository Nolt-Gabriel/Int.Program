soma = 0
pares = []
for i in range(6):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    if num % 2 == 0:

        pares.append(num)
        soma += num
        
print(f"A soma dos números pares digitados é: {soma}")
print(pares)
