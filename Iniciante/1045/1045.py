x, y, z = map(float, input().split())
lados = [x, y, z]
lados.sort(reverse=True)
a = lados[0]
b = lados[1]
c = lados[2]
if a >= b+c:
    print('NAO FORMA TRIANGULO')
elif pow(a, 2) == pow(b, 2)+pow(c, 2):
    print('TRIANGULO RETANGULO')
elif pow(a, 2) > pow(b, 2) + pow(c, 2):
    print('TRIANGULO OBTUSANGULO')
elif pow(a, 2) < pow(b, 2) + pow(c, 2):
    print('TRIANGULO ACUTANGULO')
if a == b and b == c and a == c:
    print('TRIANGULO EQUILATERO')
elif a == b or b == c:
    print('TRIANGULO ISOSCELES')
