from random import randint

jogos = []  
qtd = int(input("Quantos jogos quer gerar? "))

for j in range(qtd):
    jogo = []
    while len(jogo) < 6:
        n = randint(1, 60)
        if n not in jogo:       
            jogo.append(n)
    jogo.sort()
    jogos.append(jogo)

print("-=" * 20)
print(f"Gerando {qtd} jogos:")
for i, jg in enumerate(jogos, start=1):
    print(f"Jogo {i}: {jg}")
