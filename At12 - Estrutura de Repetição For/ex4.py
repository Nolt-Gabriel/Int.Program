# Solicita um número ao usuário
numero = int(input("Digite um número para ver sua tabuada: "))

# Mostra a tabuada de 1 a 10 usando 'for'
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
