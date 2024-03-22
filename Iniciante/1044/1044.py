x,y,z = map(float, input().split())
list = [x,y,z]
a = list[0]
b = list[1]
c = list[2]
if a + b > c and b+c > a and a+c > b:
    perimetro = a+b+c
    print('Perimetro = {:.1f}' .format(perimetro))
else:
    area = ((a+b)*c)/2
    print('Area = {:.1f}' .format(area))