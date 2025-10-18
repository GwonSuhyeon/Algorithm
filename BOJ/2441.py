N = int(input())

for i in range(N):
    if i > 0:
        print(' ' * i, end='')
        print('*' * (N - i))
    else:
        print('*' * (N - i))