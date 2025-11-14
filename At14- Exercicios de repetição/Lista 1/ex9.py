n = int(input("Digite um número inteiro positivo n: "))
soma = 0.0
for i in range(1, n+1):
    soma += 1/i
print(f"A soma dos termos de 1/1 até 1/{n} é {soma:.4f}")
