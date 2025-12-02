N = int(input())
arr = list(map(int, input().split()))

if N <= 1:
    print(0)
else:
    res = 0

    pos = arr[0]

    for i in range(1, N):
        if arr[i - 1] < arr[i]:
            res = max(res, arr[i] - pos)
        else:
            pos = arr[i]

    print(res)