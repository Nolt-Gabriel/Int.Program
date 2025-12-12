arquivo = open("./At21 - Manipulando arquivos/ex1/teste1.txt", "r")

# r - usado para ler algo
# w - usado para escrever algo, limpa todo o conteúdo anterior
# r+ - ler e escrever algo
# a - usado para acrescentar algo ao arquivo, sem apagar o arquivo anterior
# x - cria o arquivo

# Diz se o arquivo pode ser lido ou não
if arquivo.readable() == True: 

    print("O arquivo pode ser lido")

else:

    print("O arquivo não pode ser lido")

# Diz se o arquivo pode ser escrito ou não
if arquivo.writable() == True:

    print("O arquivo pode ser escrito")

else:

    print("O arquivo não pode ser escrito")


#arquivo.write("Só um testezin")
# arquivo.write("aiaiai\n")

#Cada vez que se escreve essa função ele lê uma linha do texto--
#--nunca sendo a mesma linha
print(arquivo.readline())
# print(arquivo.readline())
