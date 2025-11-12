n = int(input("Digite um número para calcular o fatorial: "))
fat = 1
k = 1
while k <= n:
    fat = fat * k
    k = k + 1
print(f"O fatorial de {n} é {fat}")
