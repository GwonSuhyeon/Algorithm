N, L = map(int, input().split())

L = str(L)
res = 1
cnt = 0

while True:
    if L not in str(res):
        cnt += 1
    
    if cnt == N:
        break

    res += 1

print(res)