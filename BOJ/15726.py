arr = list(map(int, input().split()))

res = [
    arr[0] * arr[1] / arr[2],
    arr[0] / arr[1] * arr[2]
    ]

print(int(max(res)))