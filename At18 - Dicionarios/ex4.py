jogador = {}
gols = []

jogador["nome"] = input("Nome do jogador: ")
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for p in range(partidas):
    gol = int(input(f"Gols na partida {p+1}: "))
    gols.append(gol)

jogador["gols"] = gols[:]
jogador["total"] = sum(gols)

print("-=" * 30)
print(jogador)

print("-=" * 30)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")
for i, g in enumerate(jogador["gols"]):
    print(f"  => Na partida {i+1}, fez {g} gols.")
print(f"Foi um total de {jogador['total']} gols no campeonato.")
