num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))
num4 = float(input("Digite o 4º número: "))

maior = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
if num4 > maior:
    maior = num4

print(f"O maior número é: {maior}")
