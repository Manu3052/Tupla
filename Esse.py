n = s = contador = 0
while True:
    contador += 1
    n = int(input('Insira aqui um número'))
    if n == 999:
        break
    s += n
print(f'A soma de todos os números é {s}')
print(f'A quantidade de números é {contador}')