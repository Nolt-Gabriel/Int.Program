n = int(input("Quantos termos de Fibonacci mostrar? "))
termo1 = 0
termo2 = 1
contador = 0

while contador < n:
    print(termo1, end=" ")
    proximo = termo1 + termo2
    termo1 = termo2
    termo2 = proximo
    contador += 1
print()
