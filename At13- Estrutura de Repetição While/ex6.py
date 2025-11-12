import random

numero_secreto = random.randint(0, 10)
palpites = 0
acertou = False

while not acertou:
    jogador = int(input("Adivinhe o número (entre 0 e 10): "))
    palpites += 1
    if jogador == numero_secreto:
        acertou = True
    else:
        print("Errou! Tente novamente.")

print(f"Parabéns! Você acertou com {palpites} palpites. O número era {numero_secreto}.")
