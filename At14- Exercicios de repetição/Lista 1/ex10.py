palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

letras_comuns = ""

for letra in palavra1:
    if letra in palavra2 and letra not in letras_comuns:
        letras_comuns += letra

print(f"Quantidade de letras que aparecem nas duas palavras: {len(letras_comuns)}")
print(f"Letras: {sorted(letras_comuns)}")
