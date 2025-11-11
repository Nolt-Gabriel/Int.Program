angulo = int(input("Digite o ângulo (em graus): "))

voltas = angulo // 360
angulo_normalizado = angulo % 360

if 0 < angulo_normalizado < 90:
    quadrante = "primeiro quadrante"
elif 90 < angulo_normalizado < 180:
    quadrante = "segundo quadrante"
elif 180 < angulo_normalizado < 270:
    quadrante = "terceiro quadrante"
elif 270 < angulo_normalizado < 360:
    quadrante = "quarto quadrante"
elif angulo_normalizado == 0 or angulo_normalizado == 90 or angulo_normalizado == 180 or angulo_normalizado == 270:
    quadrante = "sobre o eixo (não pertence a um quadrante)"
else:
    quadrante = "inválido"

print(f"O ângulo está no {quadrante}.")
print(f"O ângulo dá {voltas} voltas completas.")
