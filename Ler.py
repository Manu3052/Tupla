cont = ('zero', 'um','dois','três','quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze'
        ,'quartoze', 'quinze','desesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Insira um número entre 0 e 20:    '))
    if 0 <= num <= 20 :
        break 
    else:
        print('Tente novamente.Insira um número entre 0 e 20.')
print(f'O número {num} por extenso é {cont[num]}.')

