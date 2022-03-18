#Tuplas 
produtos = ('Veja', 10.99, 
            'carne', 20.90,
            'água', 0.99,
            'desinfetante', 9.60)
print('-' * 40)
print('\n           TABELA DE PREÇOS')
print('-' * 40)
for posição in range(0, len(produtos)):
    if posição % 2 == 0:
        print(f'{produtos[posição]}','-' * 20,'R$', end='')
    if posição % 2 != 0:
        print(f'{produtos[posição]}')
print('-' * 40)
