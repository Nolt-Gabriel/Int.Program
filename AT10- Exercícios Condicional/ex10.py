num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

maior = max(num1, num2)
menor = min(num1, num2)

if menorr == 0:
    print("Não é possível dividir por zero.")
elif maior % menor == 0:
    print(f"O maior número ({maior}) é múltiplo do menor ({menor}).")
else:
    print(f"O maior número ({maior}) não é múltiplo do menor ({menor}).")
