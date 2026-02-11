N, X = map(int, input().split())
arr = list(map(int, input().split()))

res = 1
tmp = 1

for i in range(N - 1):
    if arr[i + 1] - arr[i] <= X:
        tmp += 1
    else:
        tmp = 1
    
    res = max(res, tmp)

print(res)