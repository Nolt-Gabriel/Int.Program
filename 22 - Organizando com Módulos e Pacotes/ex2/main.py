import moeda  


dados = {"contador": 10, "tamanho": 5}


dados = moeda.aumentar(dados, "contador", 3)
print("Após aumentar:", dados)

dados = moeda.diminuir(dados, "tamanho", 2)
print("Após diminuir:", dados)

dados = moeda.dobrar(dados, "contador")
print("Após dobrar:", dados)
