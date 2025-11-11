arr = sorted(list(map(int, input().split())))

num = min(abs(arr[0] - arr[1]), abs(arr[1] - arr[2]))

for i in arr:
    if i + num not in arr:
        res = i + num

        break

print(res)