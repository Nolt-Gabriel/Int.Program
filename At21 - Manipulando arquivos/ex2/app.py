mensagem = open("./At21 - Manipulando arquivos/ex2/mensagem.txt", "r")
cript = open("./At21 - Manipulando arquivos/ex2/cript.txt", "w")


for linha in mensagem.readlines():

    for letra in linha:

        if letra in ("aeiouãõê"):

            cript.write("*")
        
        else:

            cript.write(letra)