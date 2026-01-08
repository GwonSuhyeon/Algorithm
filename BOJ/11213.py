n = int(input())
arr = list(map(int, input().split()))

res = 0
maximum = 0

for idx, i in enumerate(arr):
    if arr.count(i) == 1:
        if i > maximum:
            res = idx + 1
            maximum = i

if maximum > 0:
    print(res)
else:
    print('none')