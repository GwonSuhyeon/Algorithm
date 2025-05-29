N, M, L = map(int, input().split())

res = 0

people = [0 for _ in range(N)]
idx = 0

while True:
    people[idx] += 1
    
    if max(people) == M:
        break
    
    if people[idx] % 2 == 0:
        if idx - L >= 0:
            idx -= L
        else:
            idx = N - abs(idx - L)
    else:
        if idx + L < N:
            idx += L
        else:
            idx = abs(L - (N - idx))
    
    res += 1

print(res)