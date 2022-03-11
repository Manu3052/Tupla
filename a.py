while True:
    num = int(input('Insira aqui o número:  '))
    if num < 0:
        print('O número não é válido, digite um número positivo.')
        break
    print('--'* 20)
    print(f'Tabuada de {num}')
    for c in range (0, 11):
        mult = c * num
        print(f'{c} x {num}= {mult}')