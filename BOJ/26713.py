import copy


n = int(input())
arr_origin = list(map(int, input().split()))

res1 = 0
res2 = 0

arr_a = copy.deepcopy(arr_origin)
arr_b = copy.deepcopy(arr_origin)

for i in range(n - 1):
    if i % 2 == 0:
        if arr_a[i] >= arr_a[i + 1]:
            arr_a[i + 1] = 1000001

            res1 += 1
    else:
        if arr_a[i] <= arr_a[i + 1]:
            arr_a[i + 1] = -1000001

            res1 += 1

for i in range(n - 1):
    if i % 2 == 0:
        if arr_b[i] <= arr_b[i + 1]:
            arr_b[i + 1] = -1000001

            res2 += 1
    else:
        if arr_b[i] >= arr_b[i + 1]:
            arr_b[i + 1] = 1000001

            res2 += 1

print(min(res1, res2))