A, P = map(int, input().split())

Axel = A * 7
Petra = P * 13

if Axel > Petra:
    print('Axel')
elif Petra > Axel:
    print('Petra')
else:
    print('lika')