# Tupla dos 20 primeiros colocados (em ordem)
times = (
    'Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia',
    'Botafogo', 'Fluminense', 'São Paulo', 'Atlético-MG', 'Vasco',
    'Red Bull Bragantino', 'Ceará', 'Corinthians', 'Grêmio', 'Internacional',
    'Vitória', 'Santos', 'Juventude', 'Fortaleza', 'Sport'
)

# A) Os 5 primeiros
print('A) Os 5 primeiros:', times[:5])

# B) Os 4 últimos
print('B) Os 4 últimos:', times[-4:])

# C) Times em ordem alfabética
print('C) Ordem alfabética:', sorted(times))

# D) Posição da Chapecoense
if 'Chapecoense' in times:
    print('D) Posição da Chapecoense:', times.index('Chapecoense') + 1)
else:
    print('D) Chapecoense não está entre os 20 primeiros.')
