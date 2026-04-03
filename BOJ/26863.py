arr = []

for _ in range(4):
    arr.append(int(input()))

b = int(input())
arr = sorted(arr)

res = 0

if len(set(arr)) == 1:
    res = 1
else:
    arr[0] += b

    if len(set(arr)) == 1:
        res = 1

print(res)