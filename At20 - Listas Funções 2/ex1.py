from datetime import datetime

ano = datetime.today()

anot = int(ano.strftime("%Y"))

anon = int(input("Digite seu ano de nascimento: "))
valor = anot -anon

def votar (anon):

    

    if valor >=18:

        print("O seu voto é obrigatório!")
    
    elif valor < 18 and valor != 16 and valor != 17:

        print("Não pode votar ainda :(")

    elif valor == 17 or valor == 16:

        print("seu voto é opcional, ninguém se importa :D!")

votar(anon)      