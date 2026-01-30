N, M = map(int, input().split())
S = input()

for _ in range(M):
    line = input()

    res = 0

    for i in line:
        if res < N and i == S[res]:
            res += 1
    
    if res == N:
        print('true')
    else:
        print('false')