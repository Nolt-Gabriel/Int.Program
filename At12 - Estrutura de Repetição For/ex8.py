# Lê uma frase qualquer do usuário
frase = input("Digite uma frase: ")

# Remove os espaços e transforma em minúsculas
frase_formatada = frase.replace(" ", "").lower()

# Verifica se é igual ao inverso
if frase_formatada == frase_formatada[::-1]:
    print("A frase é um palíndromo!")
else:
    print("A frase NÃO é um palíndromo.")
