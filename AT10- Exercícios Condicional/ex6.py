nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")

if len(nome1) > len(nome2):
    print(f'O nome com mais caracteres é: {nome1}')
elif len(nome2) > len(nome1):
    print(f'O nome com mais caracteres é: {nome2}')
else:
    print('Os dois nomes possuem a mesma quantidade de caracteres.')
