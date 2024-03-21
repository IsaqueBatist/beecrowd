A = float(input())
B = float(input())
C = float(input())
if A+B > C and A+C > B and B+C > A:
    perimetro = A+B+C
    print('Perimetro = {}'.format(perimetro))
else:
    Area = ((A+B)*C)/2
    print('Area = {}' .format(Area))
