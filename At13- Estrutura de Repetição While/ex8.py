n = int(input("Digite um número para ver seu fatorial: "))
fat = 1
cont = n

print(f"{n}! = ", end="")
while cont > 0:
    print(f"{cont}", end="")
    if cont > 1:
        print(" x ", end="")
    fat *= cont
    cont -= 1
print(f" = {fat}")

