numeros = []


while True:
    n = int(input("Digite um número: "))
    numeros.append(n)

    op = input("Quer continuar? [S/N] ").strip().upper()
    if op == 'N':
        break


print(f"A) Foram digitados {len(numeros)} números.")


numeros.sort(reverse=True)   
print(f"B) Lista em ordem decrescente: {numeros}")


if 5 in numeros:             
    print("C) O valor 5 foi digitado e está na lista.")
else:
    print("C) O valor 5 NÃO foi digitado e não está na lista.")
