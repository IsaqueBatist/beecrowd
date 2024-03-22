x, y = map(int, input().split())
list = [x, y]
a = list[0]
b = list[1]
if a % b == 0:
    print('Sao Multiplos')
elif b % a == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
