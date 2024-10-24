N, M = map(int, input().split())

arr = [0 for _ in range(N + 1)]

for i in range(1, M + 1):
    i, j, k = map(int, input().split())

    for idx in range(i, j + 1):
        arr[idx] = k

for i in arr[1:]:
    print(i, end=' ')