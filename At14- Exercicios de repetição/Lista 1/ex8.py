# Lê os coeficientes da função
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

# Percorre o intervalo de 0 a 100
for x in range(0, 101):
    fx = a * x + b
    print(f"{x}, {fx}")
