T = int(input())

for _ in range(T):
    N, C = map(int, input().split())
    
    if N % C > 0:
        print('%d' % int((N // C) + 1))
    else:
        print('%d' % int((N // C)))