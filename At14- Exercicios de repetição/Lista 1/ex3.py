n = int(input("Digite o valor de n: "))
m = int(input("Digite o valor de m: "))

for i in range(n, m):
    if i % n == 0:
        print(i)
