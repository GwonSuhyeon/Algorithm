n, m, k = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

res = []

for i in range(1, n + 1):
    if i not in arr1 and i not in arr2:
        res.append(i)

if len(res) > 0:
    print(len(res))
    print(*res)
else:
    print(0)