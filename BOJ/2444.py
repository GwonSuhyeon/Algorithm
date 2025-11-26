N = int(input())

for i in range(N - 1):
    print(' ' * (N - i - 1), end='')
    print('*' * i, end='')
    print('*', end='')
    print('*' * i)

print('*' * (2 * N - 1))

for i in range(N - 2, -1, -1):
    print(' ' * (N - i - 1), end='')
    print('*' * i, end='')
    print('*', end='')
    print('*' * i)