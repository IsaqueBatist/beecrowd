from math import sqrt
z,y,i = map(int, input().split())
list= [z,y,i]
a=list[0]
b=list[1]
c=list[2]
x = (b*b) - 4*a*c
if 2*a == 0 or x<0:
  print('Impossível calcular')
else:
  r1 = (-b + sqrt(x))/(2*a)
  r2 = (-b - sqrt(x))/(2*a)
  print(f'R1 = {r1:.5f}')
  print(f'R2 = {r2:.5f}')
