numeros = []
numerosorganizados = []
for c in range(0, 3):
    num = int(input('numero: '))
    numeros.append(num)
    numerosorganizados.append(num)
numerosorganizados.sort()
for v in numerosorganizados:
    print('{}\n' .format(v), end='')
print()
for v in numeros:
    print('{}\n' .format(v), end='')