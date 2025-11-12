while True:
    a = int(input("Primeiro valor: "))
    b = int(input("Segundo valor: "))
    while True:
        print("""
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
""")
        op = int(input("Qual é a sua opção? "))
        if op == 1:
            print(f"A soma é {a + b}")
        elif op == 2:
            print(f"O produto é {a * b}")
        elif op == 3:
            maior = a if a > b else b
            print(f"O maior valor é {maior}")
        elif op == 4:
            break  # Volta ao início e lê novos valores
        elif op == 5:
            print("Finalizando o programa...")
            exit()
        else:
            print("Opção inválida. Tente novamente.")
