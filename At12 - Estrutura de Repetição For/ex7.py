# Lê o número inteiro
num = int(input("Digite um número inteiro: "))

# Inicializa uma variável para contar os divisores
divisores = 0

# Verifica quantos divisores o número possui
for i in range(1, num + 1):
    if num % i == 0:
        divisores += 1

# Um número primo tem exatamente dois divisores: 1 e ele mesmo
if divisores == 2:
    print(f"{num} é um número primo.")
else:
    print(f"{num} NÃO é um número primo.")
