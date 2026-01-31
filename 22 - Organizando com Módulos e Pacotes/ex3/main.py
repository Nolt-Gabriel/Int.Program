import moeda

dados = {"túnel": 3000.0}


dados = moeda.aumentar(dados, "túnel", 1500, formato='M')
dados = moeda.diminuir(dados, "túnel", 500, formato='M')
dados = moeda.dobrar(dados, "túnel", formato='M')

moeda.mostrar(dados)
