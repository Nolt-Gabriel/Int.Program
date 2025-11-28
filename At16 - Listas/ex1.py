valores = []

for i in range(5):
    
    try:
        n = int(input(f"Digite um valor para a posição {i}: "))
        valores.append(n)
    
    except:

        print("Nada foi digitado")



print(f"Você digitou: {valores}")

maior = max(valores)
menor = min(valores)

print(f"Maior valor digitado: {maior} nas posições ", end="")
for i, v in enumerate(valores):
    if v == maior:
        print(i, end=" ")

print(f"\nMenor valor digitado: {menor} nas posições ", end="")
for i, v in enumerate(valores):
    if v == menor:
        print(i, end=" ")
