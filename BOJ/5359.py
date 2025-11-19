T = int(input())

for _ in range(T):
    n, m, c = map(int, input().split())
    arr = list(map(int, input().split()))

    res = 0

    for i in range((n - m) + 1):
        slice = arr[i:i + m]

        if max(slice) - min(slice) <= c:
            res += 1

    print(res)