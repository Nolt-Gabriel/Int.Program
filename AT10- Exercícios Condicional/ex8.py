angulo = int(input("Digite o ângulo (em graus): "))

# Ajustando o ângulo para o intervalo [0, 360)
angulo_normalizado = angulo % 360

if 0 < angulo_normalizado < 90:
    print("O ângulo está no primeiro quadrante.")
elif 90 < angulo_normalizado < 180:
    print("O ângulo está no segundo quadrante.")
elif 180 < angulo_normalizado < 270:
    print("O ângulo está no terceiro quadrante.")
elif 270 < angulo_normalizado < 360:
    print("O ângulo está no quarto quadrante.")
elif angulo_normalizado == 0 or angulo_normalizado == 90 or angulo_normalizado == 180 or angulo_normalizado == 270:
    print("O ângulo está sobre o eixo (não pertence a um quadrante).")
else:
    print("Ângulo inválido.")

