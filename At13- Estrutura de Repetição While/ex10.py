primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

total = 10
contador = 1
termo = primeiro

while total != 0:
    c = 0
    while c < total:
        print(termo, end=" ")
        termo += razao
        c += 1
    print()
    total = int(input("Quantos termos a mais deseja mostrar? (0 para sair) "))

print("FIM")
