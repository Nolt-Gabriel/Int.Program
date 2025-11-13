# Tupla única com nomes de produtos e preços, na sequência
produtos = (
    'Pão', 2.50,
    'Leite', 4.00,
    'Café', 7.99,
    'Arroz', 5.60,
    'Feijão', 6.30
)

# Exibição tabular
print('-' * 30)
print(f'{"Produto":<15}{"Preço":>10}')
print('-' * 30)
for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:<15}R${produtos[i+1]:>8.2f}')
print('-' * 30)
