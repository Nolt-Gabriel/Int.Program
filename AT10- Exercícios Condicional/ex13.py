numero = float(input("Digite um número real: "))

parte_inteira = int(numero)
parte_fracionaria = numero - parte_inteira

if parte_fracionaria > 0.5:
    arredondado = parte_inteira + 1
else:
    arredondado = parte_inteira

print(f"O número arredondado é: {arredondado}")
