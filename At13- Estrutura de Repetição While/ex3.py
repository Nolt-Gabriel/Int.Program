n = int(input("Digite um número para calcular o fatorial: "))
k = 1
fat = 1
while k <= n:
    fat = fat * k
    k = k + 1
print(f"fat({n}) = {fat}")
