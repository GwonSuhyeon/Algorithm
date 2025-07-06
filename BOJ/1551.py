N, K = map(int, input().split())

arr = list(map(int, input().split(',')))

res = arr.copy()

for _ in range(K):
    res = []

    for i in range(len(arr) - 1):
        res.append(arr[i + 1] - arr[i])

    arr = res.copy()

for i in range(len(res)):
    if i < len(res) - 1:
        print(res[i], end=',')
    else:
        print(res[i])