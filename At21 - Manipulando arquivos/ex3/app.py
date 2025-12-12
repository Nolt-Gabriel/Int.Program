def ips (ip):

    ip = ip.split(".")

    for byte in ip:

        if int(byte) > 255:

            return False
    return True


arq = open("./At21 - Manipulando arquivos/ex3/arq.txt", "r")
valid = open("./At21 - Manipulando arquivos/ex3/valid.txt", "w")
invalid = open("./At21 - Manipulando arquivos/ex3/invalid.txt", "w")

for linha in arq.readlines():

    if ips(linha):

        valid.write(linha)
    
    else:

        invalid.write(linha)

arq.close()
valid.close()
invalid.close()