N = int(input())

for i in range(N):
    star = (2 * (N - i)) - 1
    
    print(' ' * i, end='')
    print('*' * star)