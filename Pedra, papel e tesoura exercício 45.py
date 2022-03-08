from random import randint 
lista = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
x = int(input('Escolha 0(pedra), 1(papel) ou 2(tesoura) e tente me vencer!'))
if computador == 0:
    if x == 0:
        print('Nós empatamos, você colocou {} e eu {}'.format(x, computador))
    elif x == 1:
        print('Você ganhou, você colocou {} e eu {}'.format(x, computador))
    elif x == 2:
        print('Você perdeu, você colocou {} e eu {}'.format(x, computador))
    else:
        print('Invalido, coloque um valor válido')
elif computador == 1:
    if x == 1:
        print('Nós empatamos, você colocou {} e eu {}'.format(x, computador))
    elif x == 0:
        print('Você ganhou, você colocou {} e eu {}'.format(x, computador))
    elif x == 2:
        print('Você perdeu, você colocou {} e eu {}'.format(x, computador))
    else:
        print('Invalido, coloque um valor válido')
elif computador == 2:
    if x == 2:
        print('Nós empatamos, você colocou {} e eu {}'.format(x, computador))
    elif x == 1:
        print('Você ganhou, você colocou {} e eu {}'.format(x, computador))
    elif x == 0:
        print('Você perdeu, você colocou {} e eu {}'.format(x, computador))
    else:
        print('Invalido, coloque um valor válido')
print('Bom jogo!')
