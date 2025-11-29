from random import randint
from time import sleep

jogo = {}


for i in range(1, 5):
    jogo[f"Jogador {i}"] = randint(1, 6)

print("Resultados:")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado.")
    sleep(0.3)


ranking = sorted(jogo.items(), key=lambda item: item[1], reverse=True)  # [web:353][web:354]

print("\nRanking:")
for pos, (jogador, valor) in enumerate(ranking, start=1):
    print(f"{pos}º lugar: {jogador} com {valor}")
