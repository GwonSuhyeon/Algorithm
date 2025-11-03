H = int(input())

for i in range(1, H - 1, 2):
    print('*' * i, end='')
    print(' ' * ((H * 2) - (i * 2)), end='')
    print('*' * i)

print('*' * (H * 2))

for i in range(H - 2, 0, -2):
    print('*' * i, end='')
    print(' ' * ((H * 2) - (i * 2)), end='')
    print('*' * i)