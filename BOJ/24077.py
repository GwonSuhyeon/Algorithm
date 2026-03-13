N, M = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

res = 0

for a in arr1:
    for b in arr2:
        if a <= b:
            res += 1

print(res)