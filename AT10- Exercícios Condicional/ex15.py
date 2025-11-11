nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")

if nome1 == nome2:
    print("Os nomes são exatamente iguais.")
elif nome1.upper() == nome2.upper():
    print("Os nomes são iguais, mas há diferença na digitação de maiúsculas/minúsculas.")
else:
    print("Os nomes são diferentes.")
