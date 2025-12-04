def leiaInt(n):
    while True:
        a = str(input(n))
        if a.isnumeric():
            return a
            break

        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar {n}.')