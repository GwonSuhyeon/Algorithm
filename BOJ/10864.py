N, M = map(int, input().split())

res = [0 for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    
    res[A - 1] += 1
    res[B - 1] += 1

for i in res:
    print(i)