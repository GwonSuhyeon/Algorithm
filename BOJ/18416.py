N = int(input())
arr = list(map(int, input().split()))

res = 1
sub = []

for i in range(N - 1):
    if arr[i] <= arr[i + 1]:
        sub.append(i)
    else:
        sub.clear()
    
    res = max(res, len(sub) + 1)

print(res)