N = int(input())

for i in range(1, ((2 * N) // 2) + 1):
    print(' ' * (i - 1), end='')
    print('*' * (N - i), end='')
    print('*', end='')
    print('*' * (N - i))

for i in range(((2 * N) // 2) - 1, 0, -1):
    print(' ' * (i - 1), end='')
    print('*' * (N - i), end='')
    print('*', end='')
    print('*' * (N - i))