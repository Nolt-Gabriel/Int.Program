primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

contador = 1
termo = primeiro

while contador <= 10:
    print(termo, end=" ")
    termo = termo + razao
    contador = contador + 1
print()
